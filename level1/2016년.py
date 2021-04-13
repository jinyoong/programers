def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    mon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    answer = ''
    d_sum = 0
    for i in range(a):
        d_sum += mon[i]
    d_sum = (d_sum + b - 1)%7
    answer = day[d_sum]
    return answer

print(solution(5, 24))