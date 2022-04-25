from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]




def bfs(board):
    q = deque([(1, 0, 0)])
    visited = set()
    visited.add((0, 0))
    time = 1
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    while q:
        for _ in range(len(q)):
            talent, y, x = q.popleft()
            if y == N - 1 and x == M - 1:
                return time
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and ((ny, nx) not in visited or (board[ny][nx] == '1' and talent == 1 and (ny, nx) in visited)):
                    if board[ny][nx] == '1' and talent == 1:
                        q.append((talent - 1, ny, nx))
                        visited.add((ny, nx))
                    elif board[ny][nx] == '0':
                        q.append((talent, ny, nx))
                        visited.add((ny, nx))
        time += 1
    return -1


result = bfs(board)
print(result)