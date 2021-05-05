'''def solution(priorities, location):
    answer = 0
    print_list = []
    l_num = -1
    while(len(priorities != 0)):
        l_num += 1
        max_num = 0
        for i in range(1, len(priorities)):
            if priorities[0] < priorities[i] :
                priorities.append(priorities[0])
                if l_num == location :
                    location = len(priorities)
                priorities.pop(0)
                break
        else:
            print_list.append(priorities[0])
            priorities.pop(0)
    return answer'''


def solution(priorities, location):
    answer = 0
    index_list = list(enumerate(priorities))
    #print(index_list)
    print_list = []
    while True:
        print('대기목록의 가장 앞에 있는 문서는 {}이고 중요도는 {}입니다.'.format(index_list[0][0], index_list[0][1]))
        for i in range(1, len(index_list)):
            temp = 0
            if index_list[0][1] < index_list[i][1]:
                print('가장 앞의 문서보다 중요도가 높은 문서가 존재합니다')
                temp = index_list[i][1]
                index_list.append(index_list[0])
                index_list.pop(0)
                break
        if temp == 0:
            if index_list[0][0] == location:
                answer += 1
                print("우리가 찾는 문서가 {}번째로 출력되었습니다.".format(answer))
                break
            index_list.pop(0)
            answer += 1
            print('대기목록의 가장 앞에 있는 문서의 중요도가 가장 크므로 {}번째로 이 문서를 출력합니다.'.format(answer))
        print('현재 바뀐 대기목록은 {}입니다.'.format(index_list))
        print()

    return answer

print(solution([1,1,9,1,1,1], 0))

def solution2(priorities, location):
    answer = 0
    index_list = list(range(len(priorities)))
    while True:
        if priorities[0] >= max(priorities[1:]):
            answer += 1
            if index_list[0] == location:
                break
            priorities.pop(0)
            index_list.pop(0)
        else:
            priorities.append(priorities[0])
            index_list.append(index_list[0])
            priorities.pop(0)
            index_list.pop(0)
    return answer

print(solution2([1,1,9,1,1,1], 0))