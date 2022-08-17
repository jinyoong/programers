def solution(relation):
    all_list = []  # 후보키를 담을 리스트
    length = len(relation[0])

    def combination(idx, count, limit, result):

        if count == limit:

            for ele in all_list:
                if set(ele).issubset(set(result)):
                    # 이전에 후보키를 만족하는 속성 또는 집합이 result 의 부분집합이라면
                    # result 는 최소성을 만족할 수 없게 되므로 comb_lst 에 포함시키지 않는다
                    return

            comb_lst.append(result)
            return

        for i in range(idx, len(relation[0])):
            combination(i + 1, count + 1, limit, result + [i])

    for l in range(1, length + 1):
        comb_lst = []  # 인덱스 조합을 담을 리스트
        combination(0, 0, l, [])

        for comb_ele in comb_lst:
            temp_lst = []  # 현재까지 선택된 튜플들을 담을 리스트
            for relation_ele in relation:
                item = [relation_ele[k] for k in comb_ele]  # 선택된 속성 또는 속성 집합으로 만들어진 튜플

                if item in temp_lst:  # 중복되는 튜플이 존재하면 유일성을 만족하지 못하니까 멈춘다
                    break

                temp_lst += [item]

            else:
                all_list += [comb_ele]

    return len(all_list)


print(solution([["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]]))
