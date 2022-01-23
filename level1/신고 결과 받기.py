def solution(id_list, report, k):
    answer = [0] * len(id_list)

    id_dict = {}

    idx = 0
    for id in id_list:
        id_dict[id] = idx
        idx += 1

    singo_lst = [[0] * len(id_list) for _ in range(len(id_list))]

    for ele in report:
        singoza, p_singoza = ele.split()
        singo_lst[id_dict[p_singoza]][id_dict[singoza]] = 1

    for i in range(len(id_list)):
        if sum(singo_lst[i]) >= k:
            for j in range(len(id_list)):
                if singo_lst[i][j]:
                    answer[j] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
