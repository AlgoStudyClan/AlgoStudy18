def solution(name):
    
    answer = 0    
    
    for i in range(len(name)):
        if i >= 1:            
            if name[i] == 'A' and i == 1:
                continue
            else:
                answer += 1          
        if ord(name[i]) >= 78:
            answer += 91 - ord(name[i])
        else:
            answer += ord(name[i]) - 65
        
    return answer