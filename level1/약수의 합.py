def solution(n):
    answer = 0
    for i in range(1, round(n**0.5)+1):
        if(i*i == n):
            answer += i
        elif(n%i == 0):
            answer += i + int(n/i)
    return answer

print(solution(9))