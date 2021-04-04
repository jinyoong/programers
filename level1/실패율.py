def solution(N, stages):
    answer = []
    s_list = []
    #print(stages)
    for i in range(N):
        f_ct = 0
        s_ct = 0
        j = 0
        for j in range(len(stages)):
            if(stages[j] >= i+1):
                s_ct += 1
                if(stages[j] < i+2):
                    f_ct += 1
        #print('{}번 스테이지 도달 수 = {}, 클리어 수 = {}'.format(i,s_ct,f_ct))
        if(s_ct == 0):
            s_list.append(0)
        else:
            s_list.append(f_ct/s_ct)
    #print(s_list)
    #s_list.sort(key=lambda x:x[1], reverse=True)
    '''for k in range(N):
        answer += [s_list[k][0]]'''
    #answer = list(zip(*s_list))[0]
    while(N > 0):
        max_rate = 0
        ct = 0
        for k in range(len(s_list)):
            if(max_rate < s_list[k]):
                max_rate = s_list[k]
        #print(s_list.index(max_rate)+1)
        answer += [s_list.index(max_rate)+1]
        s_list[s_list.index(max_rate)] = -1
        N -= 1
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(5, [4,4,4,4,4]))