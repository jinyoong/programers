def solution(n):
    n = str(n)
    answer = 0
    for num in n:
        answer += int(num)
    return answer


print(solution(123))