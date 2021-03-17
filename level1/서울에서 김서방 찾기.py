def solution(seoul):
    count = 0
    for i in range(len(seoul)):
        if(seoul[i] == 'Kim'):
            return '김서방은 {}에 있다'.format(i)


solution(['Lee', 'Park', 'Kim'])