def solution(dartResult):
    answer = 0
    dart_pt = []
    prize = ['*', '#']
    s_sum = []
    score = -1
    alpha_sc = -1
    for i in range(len(dartResult)):
        score += 1
        if(dartResult[i] == 'S'):
            s_sum += [int(dartResult[alpha_sc+1:score])]
            alpha_sc = score
        elif(dartResult[i] == 'D'):
            s_sum += [int(dartResult[alpha_sc+1:score])**2]
            alpha_sc = score
        elif(dartResult[i] == 'T'):
            s_sum += [int(dartResult[alpha_sc+1:score])**3]
            alpha_sc = score
        elif(dartResult[i] in prize):
            s_sum += [dartResult[i]]
            alpha_sc = score
    print(s_sum)
    if(len(s_sum) == 3):
        for s in s_sum:
            answer += s
    else:
        for j in range(len(s_sum)):
            dart_pt += [s_sum[j]]
            if(s_sum[j] == prize[0]):
                k = j
                ct = 0
                while(k != 0 and ct != 2):
                    k -= 1
                    if(type(s_sum[k]) == int):
                        dart_pt[k] = dart_pt[k] * 2
                        ct += 1
            elif(s_sum[j] == prize[1]):
                dart_pt[j-1] = dart_pt[j-1] *(-1)
    print(dart_pt)
    for v in dart_pt:
        if(type(v) == int):
            answer += v
    return answer

#다른 사람 풀이


import re

def solution2(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


print(solution('1T2D*3D#'))
print(solution('1D2S#10S'))