def solution(lottos, win_nums):
    winSet = set()
    winSet.update(win_nums)
    zeros = 0
    same = 0
    for num in lottos:
        if num == 0:
            zeros += 1
        elif num in winSet:
            same += 1
    rank_table = {7 - i : i for i in range(6+1)}
    rank_table[0] = 6
    return [rank_table[same + zeros], rank_table[same]]