def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    num = [a,b,c]
    best = []
    answer = []
    for man in num:
        count = 0
        x,y = divmod(len(answers), len(man))
        test = man*x
        for i in range(y):
            test.append(man[i])
        for j in range(len(answers)):
            if(answers[j] == test[j]):
                count += 1
        best.append(count)
    for k in range(1,4):
        if(best[k-1] == max(best)):
            answer.append(k)
    return answer


print(solution([1,2,3,4,5]))