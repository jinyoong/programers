def solution(skill, skill_trees):

    answer = len(skill_trees)
    # 안 되는 스킬트리가 나올 경우 1씩 빼갈 것
    s_list = list(skill)
    # 찍어야 하는 스킬트리 순서를 리스트로 설정한다.

    for i in skill_trees:
        temp = s_list.copy()
        # 각 스킬트리의 경우마다 순서 리스트를 사용할 것이므로 temp 배열에 복사한다.
        # print('{}스킬트리가 가능한지 살펴봅니다.'.format(i))

        for j in i:
            # print('{}스킬트리의 {}스킬부터 살펴봅니다.'.format(i, j))

            if j in temp:

                if j == temp[0]:
                    # print('{}스킬을 찍을 수 있습니다.'.format(j))
                    temp.pop(0)
                    # 만약 j번째 스킬이 스킬트리에 포함된 스킬이면서 순서에 맞다면 찍을 수 있는 것
                    # 이미 찍은 스킬은 temp 배열에서 제거한다.
                else:
                    # print('{}스킬트리는 불가능합니다.'.format(i))
                    answer -= 1
                    break

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))