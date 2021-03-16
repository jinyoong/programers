def solution(a, b):
    answer = 0
    mean_two = float((a+b)/2)
    count = abs(a-b)+1
    if(a != b):
        answer = int(mean_two*count)
    else:
        answer = a
    return answer


print(solution(9, 6))