from functools import lru_cache
@lru_cache(maxsize=None)
def unique(word):
    if type(word) == str:
        c = 0
        s = {}
        for i in word:
            s[i] = word.count(i)
        return len([i for i, j in s.items() if j == 1])
    else:
        return 'TypeError'