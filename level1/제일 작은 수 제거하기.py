def solution(arr):
    answer = []
    mini = arr[0]
    if(len(arr) == 1):
        answer.append(-1)
        return answer
    else:
        for i in range(1, len(arr)):
            if(mini > arr[i]):
                mini = arr[i]
        arr.remove(mini)
        return arr


print(solution([4,3]))