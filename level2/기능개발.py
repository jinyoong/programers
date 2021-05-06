def solution(progresses, speeds):
    answer = []
    pre_progress = 0
    count = 0
    finish_ct = 0
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            progress = int((100 - progresses[i]) / speeds[i])
        else:
            progress = int((100 - progresses[i]) / speeds[i]) + 1
        print('{}번 기능이 완성되는데 걸리는 시간은 {}입니다.'.format(i+1, progress))
        if i == 0:
            pre_progress = progress
            count = i
            continue
        else:
            if pre_progress >= progress:
                print('{}번 기능개발이 끝날 때 같이 끝납니다.'.format(count + 1))
            else:
                answer.append(i - count)
                count = i
                pre_progress = progress
    answer.append(i - count + 1)
    return answer



print(solution(	[95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print()
print(solution([70,80,40,50,60,20,10,10,10,10], [5,4,6,2,4,7,2,3,4,9]))