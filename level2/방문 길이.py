def solution(dirs):
    answer = 0

    past_road = []

    character_pt = [0, 0]

    move_dic = {'U' : [0, 1], 'D' : [0, -1], 'R' : [1, 0], 'L' : [-1, 0]}

    for i in dirs:

        temp = [0, 0]
        past_temp = [0, 0]
        print('\n현재 명령어는 {}이고 {}만큼 변합니다.'.format(i, move_dic[i]))

        if abs(character_pt[0] + move_dic[i][0]) == 6 or abs(character_pt[1] + move_dic[i][1]) == 6:
            print('현재 명령어를 실행하면 좌표평면의 경계를 넘어가므로 넘어갑니다.')
            continue
        else:
            temp[0] = character_pt[0] + move_dic[i][0]
            temp[1] = character_pt[1] + move_dic[i][1]

        print('\n명령어를 실행하여 이동한 좌표는 {}입니다.'.format(temp))
        past_temp[0] = character_pt
        past_temp[1] = temp

        if past_temp in past_road or past_temp[::-1] in past_road:
            pass
        else:
            past_road.append(past_temp)

        print('지금까지 겹치지 않고 이동한 좌표는 {}입니다.'.format(past_road))
        character_pt = temp

    answer = len(past_road)
    return answer

# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
print(solution('LRLRL'))