"""Local, fictional SOC analysis. No scanning, account changes or real logs."""
from datetime import datetime, timezone

POLICY={'analyst':{'read_redacted'},'responder':{'read_redacted','propose_containment'}}
def authorized(role, action):
    return action in POLICY.get(role,set())

def triage(events, threshold=3):
    if type(threshold) is not int or threshold<1: raise ValueError('Positive integer threshold required')
    counts={}
    for event in events:
        # This is a count rule, not an inference about an attack or a person.
        if event.get('outcome')=='failed':
            actor=event.get('actor_alias')
            if not isinstance(actor,str) or not actor: raise ValueError('Fictional actor alias required')
            counts[actor]=counts.get(actor,0)+1
    return [{'actor_alias':a,'failed_count':n,'disposition':'investigate'} for a,n in sorted(counts.items()) if n>=threshold]

def timeline(events):
    def time_of(event):
        value=datetime.fromisoformat(event['time'].replace('Z','+00:00'))
        if value.tzinfo is None:raise ValueError('Explicit timezone required')
        return value.astimezone(timezone.utc)
    return sorted(events,key=time_of)
