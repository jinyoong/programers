def solution(numbers, hand):
    answer = ''
    other = [2,5,8,0]
    lh = [1,4,7]
    l_roc = [3,0]
    r_roc = [3,0]
    rh = [3,6,9]
    for num in numbers:
        if(num in lh):
            answer += 'L'
            l_roc[0] = lh.index(num)
            l_roc[1] = 0
        elif(num in rh):
            answer += 'R'
            r_roc[0] = rh.index(num)
            r_roc[1] = 0
        else:
            if(abs(other.index(num)-l_roc[0]) + abs(l_roc[1]-1) < abs(other.index(num)-r_roc[0]) + abs(r_roc[1]-1)):
                answer += 'L'
                l_roc[0] = other.index(num)
                l_roc[1] = 1
            elif(abs(other.index(num)-l_roc[0]) + abs(l_roc[1]-1) > abs(other.index(num)-r_roc[00]) + abs(r_roc[1]-1)):
                answer += 'R'
                r_roc[0] = other.index(num)
                r_roc[1] = 1
            else:
                if(hand == 'left'):
                    answer += 'L'
                    l_roc[0]= other.index(num)
                    l_roc[1] = 1
                elif(hand == 'right'):
                    answer += 'R'
                    r_roc[0] = other.index(num)
                    r_roc[1] = 1
        print('왼손은 {}에 위치'.format(l_roc))
        print('오른손은 {}에 위치'.format(r_roc))
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))