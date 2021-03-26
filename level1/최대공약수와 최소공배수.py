def solution(n, m):
    answer = []
    big = 0
    small = 0
    s_num = []
    if(n>m):
        n, m = m, n
    if(m%n == 0):
        small = n
        big = m
        answer += [small, big]
    else:
        for i in range(1, round(n**0.5)+1):
            if(n%i == 0):
                s_num += [i, int(n/i)]
        s_num.sort(reverse=False)
        for j in range(len(s_num)):
            if(m%s_num[-(j+1)] == 0):
                small = s_num[-(j+1)]
                big = small * int(n/small) * int(m/small)
                answer += [small, big]
                break
    return answer

print(solution(8, 12))