a = list(map(int, input().strip().split()))
square = [list(map(int,input().strip())) for i in range(a[0])]
max_size = min(a)
answer = 0

for i in range(a[0]):
    for j in range(a[1]):
        for k in range(max_size):
            if((i + k) < a[0]) and ((j + k) < a[1]) and (square[i][j] == square[i][j+k] == square[i+k][j] == square[i+k][j+k]):
                answer = max(answer, (k+1)*(k+1))

print(answer)