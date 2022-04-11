def solution(lottos, win_nums):
    answer = []    
    
    count = 7
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count -= 1
        elif lottos[i] == 0:
            count -= 1
    if count == 7:
        count = 6
    answer.append(count)
    
    count = 7
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count -= 1
    if count == 7:
        count = 6        
    answer.append(count)
            
        
    return answer