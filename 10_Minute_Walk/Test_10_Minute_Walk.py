def is_valid_walk(walk):
    return walk.count('s') == walk.count('n') and walk.count('w') == walk.count('e') and len(walk) == 10

def test_answer():
    walks = [['n','e','s'],['n','n','e','s','e','n','w','w','s','s'],['n','n','n','s','s','s','e','e','w','w'],['e','e','e','e']]
    answers = [False, True, True, False]
    for i in range(len(walks)):
        walk = is_valid_walk(walks[i])
        assert  walk == answers[i]
        assert type(walk) is bool