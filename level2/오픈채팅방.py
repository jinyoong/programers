def solution(record):
    answer = []

    user_dic = {}
    record_list = []

    for i in record:
        i = i.split(" ")
        if i[0] != 'Change':
            record_list.append(i[:2])
        if i[0] == 'Leave':
            continue
        if i[1] not in user_dic:
            user_dic[i[1]] = i[2]
        else:
            user_dic[i[1]] = i[2]


    print(record_list)
    print(user_dic)

    for i in record_list:
        if i[0] == 'Enter':
            answer.append(user_dic[i[1]] + '님이 들어왔습니다.')
        else:
            answer.append(user_dic[i[1]] + '님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))

'''a = {}
a['asd'] = 'kim'
print(a)
if 'asd' in a:
    a['asd'] = 'part'
print(a)'''