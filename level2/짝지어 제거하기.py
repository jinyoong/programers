'''start = 0
def solution(s):
    global start
    num = len(s)
    print('{} 중에서 같은 알파벳이 2번 연속 있는지 확인합니다.'.format(s))
    temp = s
    for i in range(start, len(s)-1):
        if s[i] == s[i+1] and i == len(s)-2:
            print('{}에서 {}이(가) 2번 연속되서 제거하고 남은 문자열을 반환합니다.'.format(s, s[i], s[:i]))
            s = s[:i]
            start = max(i-1, 0)
            break
        elif s[i] == s[i+1]:
            print('{}에서 {}이(가) 2번 연속되서 제거하고 남은 문자열을 반환합니다.'.format(s, s[i], s[:i]+s[i+2:]))
            s = s[:i] + s[i+2:]
            start = max(i-1, 0)
            break
    ch_num = len(s)
    print('함수를 통과하여 문자열이 {}으로(로) 바뀌었습니다.\n'.format(s))
    if num == ch_num:
        if ch_num != 0:
            return 0
        else:
            return 1
    else:
        return 1 * solution(s)



print(solution('ababa'))'''


'''start = 0
def solution(s):
    #global start
    num = len(s)
    print('{} 중에서 같은 알파벳이 2번 연속 있는지 확인합니다.'.format(s))
    temp = s
    for i in range(start, len(s)-1):
        if s[i] == s[i+1] and i == len(s)-2:
            print('{}에서 {}이(가) 2번 연속되서 제거하고 남은 문자열을 반환합니다.'.format(s, s[i], s[:i]))
            s = s.replace(s[i]+s[i], '  ')
            #start = max(i-1, 0)
        elif s[i] == s[i+1]:
            print('{}에서 {}이(가) 2번 연속되서 제거하고 남은 문자열을 반환합니다.'.format(s, s[i], s[:i]+s[i+2:]))
            s = s.replace(s[i]+s[i], '  ')
            #start = max(i-1, 0)
    s = s.replace(' ', '')
    ch_num = len(s)
    print('함수를 통과하여 문자열이 {}으로(로) 바뀌었습니다.\n'.format(s))
    if num == ch_num:
        if ch_num != 0:
            return 0
        else:
            return 1
    else:
        return 1 * solution(s)'''

def solution(s):
    temp = []
    for i in range(len(s)):
        if not temp :
            temp.append(s[i])
        else:
            if temp[-1] != s[i] :
                temp.append(s[i])
            else:
                temp.pop()
    if not temp :
        return 1
    else:
        return 0



print(solution('baba'))