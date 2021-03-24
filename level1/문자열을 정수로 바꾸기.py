def solution(s):
    answer = 0
    if(s[0] == '-'):
        s = s[1:]
        answer = 0-int(s)
    else:
        answer = int(s)
    return answer

print(solution('-1234'))