def solution(msg):
    answer = []

    alpha_dic = {}
    alpha_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(alpha_string)):
        alpha_dic[alpha_string[i]] = i + 1

    ct = 27
    start_pt = 0


    while start_pt < len(msg):
        finish_pt = len(msg)

        while msg[start_pt: finish_pt] not in alpha_dic:
            finish_pt -= 1
        # print(start_pt, finish_pt, msg[start_pt:finish_pt])

        if msg[start_pt:finish_pt + 1] not in alpha_dic:
            alpha_dic[msg[start_pt:finish_pt + 1]] = ct
            ct += 1
        answer.append(alpha_dic[msg[start_pt:finish_pt]])
        start_pt = finish_pt

    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABCABCDABCDE'))