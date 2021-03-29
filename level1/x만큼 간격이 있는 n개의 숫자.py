def solution(x, n):
    answer = []
    for i in range(n):
        answer += [x*(i+1)]
    return answer

print(solution(-4, 2))