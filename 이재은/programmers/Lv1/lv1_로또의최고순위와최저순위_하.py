def solution(l, w):
    erased = l.count(0)
    same = len(set(l).intersection(w))
    return [7-(erased+same) if 7-(erased+same) != 7 else 6, 7-same if 7-same <= 6 else 6]