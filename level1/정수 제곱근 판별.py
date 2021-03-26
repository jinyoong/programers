def solution(n):
    answer = 0
    for i in range(1, int(n/2)+2):
        if(i*i == n):
            answer = (i+1)**2
            break
    else:
        answer = -1
    return answer

#다른 사람 풀이 응용
def solution2(n):
    answer = 0
    if((n**0.5)%1 == 0):
        #0.0도 0과 같다고 나온다.
        #소수는 1로 나누어 떨어지지 않는걸 이용
        answer = (int(n**0.5) + 1)**2
    else:
        answer = -1
    return answer

print(solution(1))