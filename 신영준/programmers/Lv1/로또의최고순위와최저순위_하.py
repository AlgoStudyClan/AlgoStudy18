def score(x):                       # 일치하는 번호 개수
    return 6-(max(x,1))+1           # 일치하는 번호가 0개일 땐 7등이 아니라 6등

def solution(lottos, win_nums):
    i = 0                           # 일치하는 번호 개수

    for x in lottos:
        if x in win_nums:
            i += 1
    return [score(i+lottos.count(0)), score(i)]
    # 최고 순위 개수 : 일치하는 번호 개수 + 0의 개수
    # 최저 순위 개수 : 일치하는 번호 개수