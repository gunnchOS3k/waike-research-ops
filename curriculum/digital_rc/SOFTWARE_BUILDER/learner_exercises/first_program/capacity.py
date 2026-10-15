"""Fictional whole-GiB capacity example; no disk access or external dependencies."""
def capacity(total, used, reserve):
    if any(type(value) is not int for value in (total, used, reserve)):
        raise TypeError('capacities must be whole-number GiB values')
    if total <= 0:
        raise ValueError('total must be positive')
    if used < 0 or reserve < 0 or used + reserve > total:
        raise ValueError('used and separate reserve must fit within total')
    free_percent = (total - used - reserve) / total * 100
    if free_percent >= 15:
        policy = 'meets'
    else:
        policy = 'below'
    return {'free_percent': free_percent, 'policy': policy}

if __name__ == '__main__':
    result = capacity(256, 180, 12)
    print(f"Usable free: {result['free_percent']:.3f}%; {result['policy']} fixture policy")
