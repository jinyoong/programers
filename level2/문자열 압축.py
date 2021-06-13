def solution(s):
    answer = len(s)

    for i in range(1, int(len(s) / 2) + 1):
        s_list = []
        temp = 0
        # print('문자열을 {}개 단위로 잘라 압축합니다.'.format(i))
        for j in range(0, len(s), i):
            # print('{}를 봅니다.'.format(s[j:j + i]))
            if not s_list or s_list[-1][0] != s[j:j + i]:
                s_list.append([s[j:j + i], 1])
            elif s_list[-1][0] == s[j:j + i]:
                s_list[-1][1] += 1
            else:
                continue
        # print(s_list)
        for k in s_list:
            if k[1] != 1:
                temp = temp + len(k[0]) + len(str(k[1]))
            else:
                temp = temp + len(k[0])

        # print(temp)
        if answer >= temp:
            answer = temp

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))