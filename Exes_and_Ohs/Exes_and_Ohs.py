def xo(s):
    return s.count('x')+s.count('X') == s.count('o')+s.count('O')

strings = "ooxx","xxooxx","zpzpzpp","zzoo","xoxmaoxo"

for string in strings:
    print(xo(string))
