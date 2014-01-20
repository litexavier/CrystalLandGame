import random

def random_pick(items):
    sz = len(items)
    return items[random.randint(0, sz-1)]

