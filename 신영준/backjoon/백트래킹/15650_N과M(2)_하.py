N, M = map(int, input().split())     # 자연수 N, M 입력
s = []                               # 수열을 담을 list 생성

def dfs(start):
    if len(s) == M:                  # 만약 s의 길이가 구해야하는 길이와 같으면
        print(' '.join(map(str, s))) # 각 수열은 공백으로 구분하여 출력
        return

    for i in range(start, N+1):
        if i not in s:  # 같은 숫자 중복 제거 조건
            s.append(i) # 방문한 Node를 s에 추가
            dfs(i+1)    # 방문한 Node를 파라미터로 전달하여 이것보다 큰 것만 방문
            s.pop()     # 이전 상태로 돌리기 위해 pop() 함수 실행
dfs(1)