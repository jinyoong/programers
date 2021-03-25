def solution(n):
    answer = []
    n = str(n)
    for num in n:
        answer.append(int(num))
    answer.reverse()
    return answer

print(solution(153))