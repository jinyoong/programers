def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if(arr[i]%divisor == 0):
            answer.append(arr[i])
            answer.sort()
    if(answer == []):
        answer.append(-1)
    return answer


print(solution([5, 35, 6, 10], 5))