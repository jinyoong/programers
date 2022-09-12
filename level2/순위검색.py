# def solution(info, query):
#     point_dict = {"-": 0, "cpp": 1, "java": 2, "python": 3,
#                   "backend": 10, "frontend": 20,
#                   "junior": 100, "senior": 200,
#                   "chicken": 1000, "pizza": 2000}
#
#     info_length = len(info)
#     query_length = len(query)
#     answer = [0 for _ in range(query_length)]
#
#     info_list = [[0, 0] for _ in range(info_length)]
#     query_list = [[0, 0] for _ in range(query_length)]
#
#     for i in range(info_length):
#         temp_lst = info[i].split(" ")
#         point = 0
#         for j in range(4):
#             point += point_dict[temp_lst[j]]
#         info_list[i][0] = point
#         info_list[i][1] = int(temp_lst[4])
#
#     print(info_list)
#
#     for i in range(query_length):
#         temp_lst = query[i].split(" ")
#         point = 0
#         for j in range(7):
#             point += point_dict.get(temp_lst[j], 0)
#         query_list[i][0] = point
#         query_list[i][1] = int(temp_lst[7])
#
#     print(query_list)
#
#     return answer


def solution(info, query):
    answer = [0 for _ in range(len(query))]

    info_list = [[] for _ in range(len(info))]
    for i, ele in enumerate(info):
        info_list[i] = ele.split(' ')

    info_list = sorted(info_list, key=lambda x: -int(x[4]))

    for idx, choice in enumerate(query):
        choice = choice.split(' ')

        temp_answer = 0
        for i in info_list:
            if int(i[-1]) < int(choice[-1]):
                break

            result = set(choice[:7]) - set(i[:4])
            if result == {'and'} or result == {'-', 'and'}:
                temp_answer += 1

        answer[idx] = temp_answer

    return answer


print(
    solution(["java backend junior pizza 150",
              "python frontend senior chicken 210",
              "python frontend senior chicken 150",
              "cpp backend senior pizza 260",
              "java backend junior chicken 80",
              "python backend senior chicken 50"],
             ["java and backend and junior and pizza 100",
              "python and frontend and senior and chicken 200",
              "cpp and - and senior and pizza 250",
              "- and backend and senior and - 150",
              "- and - and - and chicken 100",
              "- and - and - and - 150"]
             )
)
