def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # i번째 index는 i-1 indexing에서 end는 포함하지 않기 때문에 (j-1)번째에 +1을 해줘서 j까지 잘라낸다.
        new_arr = array[i-1 : j]
        # sort () 함수를 이용하여 잘라낸 배열 정렬
        new_arr.sort()
        # k번째(index k-1) 값을 answer 배열에 추가
        answer.append(new_arr[k-1])
    return answer