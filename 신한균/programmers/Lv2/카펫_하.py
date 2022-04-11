def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    max = 0
        for i in range(1,int(sum**0.5)+1):
            if sum % i == 0:
                max = i
        answer.append(sum//max)
        answer.append(max)
            
    return answer