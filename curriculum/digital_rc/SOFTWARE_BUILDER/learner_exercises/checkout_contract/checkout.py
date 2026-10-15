"""Local worked example: deterministic checkout contract, Python 3.11+.

No HTTP listener or real identity. Caller-supplied role is a teaching input,
not authentication. Use only fictional item IDs and SQLite in-memory data.
"""
import sqlite3

class Checkout:
    def __init__(self):
        self.db = sqlite3.connect(':memory:')
        self.db.execute('CREATE TABLE items (id TEXT PRIMARY KEY, available INTEGER NOT NULL CHECK(available IN (0,1)))')
        self.db.execute('INSERT INTO items VALUES (?,?)', ('demo-1', 1))
        self.db.commit()
        self.events = []

    def request(self, method, item_id, role='reader'):
        if method not in ('GET', 'POST'):
            return self._reply(405, 'method_not_allowed')
        if role not in ('reader', 'desk'):
            return self._reply(403, 'forbidden')
        if method == 'POST' and role != 'desk':
            return self._reply(403, 'forbidden')
        row = self.db.execute('SELECT available FROM items WHERE id=?', (item_id,)).fetchone()
        if row is None:
            return self._reply(404, 'not_found')
        if method == 'GET':
            return self._reply(200, 'available' if row[0] else 'checked_out')
        # Conditional update enforces the state transition in this local fixture.
        # This single-connection example does not establish multi-client behavior.
        with self.db:
            changed = self.db.execute('UPDATE items SET available=0 WHERE id=? AND available=1', (item_id,)).rowcount
        return self._reply(201, 'checkout_created') if changed else self._reply(409, 'already_checked_out')

    def _reply(self, status, outcome):
        self.events.append({'status': status, 'outcome': outcome})
        return {'status': status, 'outcome': outcome}

    def close(self):
        self.db.close()
