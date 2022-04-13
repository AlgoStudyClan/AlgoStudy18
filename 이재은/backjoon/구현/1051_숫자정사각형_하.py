a = list(map(int, input().strip().split()))
square = [list(map(int,input().strip())) for i in range(a[0])]
max_size = min(a)

def fun(max_size, square, a):
    while(max_size > 0):
        print('max',max_size)
        for j in range(a[0]-max_size+1):
            for i in range(a[1]-max_size+1):
                print(i,j)
                if square[j][i] == square[j+max_size-1][i+max_size-1] == square[j][i+max_size-1] == square[j+max_size-1][i]:
                    return max_size*max_size
        max_size -= 1

answer = fun(max_size, square, a)
print(answer)