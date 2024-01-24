def is_valid_walk(walk):
    return walk.count('s') == walk.count('n') and walk.count('w') == walk.count('e') and len(walk) == 10