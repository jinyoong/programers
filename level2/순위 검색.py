def solution(info, query):
    answer = []
    a = [1, 3, 5, 7, 9, 20, 40, 6]

    return answer


def solution2(info, query):
    answer = []

    info_list = []

    for n in info:
        info_list.append(n.split(' '))

    print('지원자 정보는 아래와 같습니다.')
    for i in info_list:
        print(i)
    print()

    for choice in query:
        choice = choice.replace('and ', '')
        choice = choice.split(' ')
        # print('\n{} 조건에 맞는 지원자가 있는지 확인합니다.'.format(choice))
        in_list = info_list.copy()
        for i in range(len(choice)):
            if choice[i] == '-':
                continue
            # print('현재 남은 지원자는 {}입니다.'.format(in_list))
            # print('{} 조건에 부합하는 지원자가 있는지 찾아봅니다.'.format(choice[i]))

            temp = []

            if not choice[i].isdigit():
                for j in in_list:
                    if choice[i] == j[i]:
                        # print('{} 지원자가 {} 조건을 가지고 있습니다.'.format(j, choice[i]))
                        temp.append(j)

            else:

                for j in in_list:
                     if int(choice[i]) <= int(j[i]):
                            temp.append(j)
            in_list = temp

        answer.append(len(temp))

    return answer

def solution3(info, query):
    answer = []

    info_list = []
    for i in info:
        info_list.append(i.split(' '))

    print(info_list)
    info_list = sorted(info_list, key=lambda x: -int(x[4]))

    print(info_list)

    for choice in query:
        choice = choice.replace('and ', '')
        choice = choice.split(' ')
        print('\n{} 조건에 맞는 지원자가 있는지 확인합니다.'.format(choice))

        finish_index = 0
        print('점수부터 통과했는지 확인합니다.')
        for i in info_list:
            if int(i[-1]) >= int(choice[-1]):
                finish_index += 1
            else:
                break
        print(finish_index)
        print('점수를 통과한 지원자는 {}명 입니다.'.format(finish_index + 1))

        print('점수를 제외한 다른 조건을 통과했는지 확인합니다.')
        temp_answer = 0
        for i in range(finish_index):
            if not set(choice[:4]) - set(info_list[i][:4]) or set(choice[:4]) - set(info_list[i][:4]) == {'-'}:
                print('모든 조건을 통과한 지원자는 {}입니다.'.format(info_list[i]))
                temp_answer += 1
        answer.append(temp_answer)

    return answer


'''in_list = info_list.copy()
for i in range(len(choice)):
    if choice[i] == '-':
        continue
    # print('현재 남은 지원자는 {}입니다.'.format(in_list))
    # print('{} 조건에 부합하는 지원자가 있는지 찾아봅니다.'.format(choice[i]))

    temp = []

    if not choice[i].isdigit():
        for j in in_list:
            if choice[i] == j[i]:
            # print('{} 지원자가 {} 조건을 가지고 있습니다.'.format(j, choice[i]))
                temp.append(j)

    else:

        for j in in_list:
             if int(choice[i]) <= int(j[i]):
                    temp.append(j)
    in_list = temp

answer.append(len(temp))'''



print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
               ,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))