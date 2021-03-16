def solution(n):
    cha = []
    answer = 0
    while(n>2):
        n, y = divmod(n, 3)
        cha.append(y)
    cha.append(n)
    #print(cha)
    for i in range(len(cha)):
        answer += cha[-i-1]*3**i
    return answer


print(solution(45))