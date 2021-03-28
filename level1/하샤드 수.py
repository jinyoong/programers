def solution(x):
    answer = True
    x_sum = 0
    y = str(x)
    for i in y:
        x_sum += int(i)
    if(x%x_sum == 0):
        return answer
    else:
        return not answer

print(solution(18))