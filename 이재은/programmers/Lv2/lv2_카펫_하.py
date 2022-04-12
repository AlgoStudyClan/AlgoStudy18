def solution(b, y):
    carpet = (b-4)//2
    
    for i in range(1, carpet//2 + 1):
        j = carpet - i
        if i * j == y:
            break
    
    return [j+2, i+2]