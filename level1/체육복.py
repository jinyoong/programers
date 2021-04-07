def solution(n, lost, reserve):
    answer = 0
    max_ct = n-len(lost)
    ct = 0
    self = lost.copy()
    for i in range(len(lost)):
        if(lost[i] in reserve):
            del reserve[reserve.index(lost[i])]
            self.remove(lost[i])
            print('{}번 학생은 자신의 여벌 체육복을 사용\n남은 체육복을 가진 학생은 {}'.format(lost[i], reserve))
            ct += 1
    for j in range(len(self)):
        if(self[j]-1 in reserve):
            del reserve[reserve.index(self[j]-1)]
            ct += 1
            print('{}번 학생은 {}번 학생의 여벌 체육복을 사용\n남은 체육복을 가진 학생은 {}'.format(lost[j], self[j]-1,reserve))
        elif(self[j]+1 in reserve):
            del reserve[reserve.index(self[j]+1)]
            ct += 1
            print('{}번 학생은 {}번 학생의 여벌 체육복을 사용\n남은 체육복을 가진 학생은 {}'.format(lost[j], self[j]+1,reserve))
    answer += max_ct + ct
    return answer

print(solution(10, [2,3,4], [1,3,5]))