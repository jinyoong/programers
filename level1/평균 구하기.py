def solution(arr):
    answer = 0
    arr_sum = 0
    for i in arr:
        arr_sum += i
    answer = arr_sum/len(arr)
    return answer

print(solution([1,2,3,4]))