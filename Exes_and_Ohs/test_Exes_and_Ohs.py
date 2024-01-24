import pytest

def xo(s):
    return s.count('x')+s.count('X') == s.count('o')+s.count('O')

def test_answer():
    strings = 'xxoo','oxoXfhsdaflkjqxjaasdfOfhexO','asdfjklh','dhxkdjeiOx'
    answers = True,True,True,False
    for i in range(len(strings)):
        assert xo(strings[i]) == answers[i]
    assert xo('xxoo') is bool
