def solution(orders, course):
    answer = []

    def menu_combi(length, idx, cnt, limit, result):
        nonlocal word_list

        if cnt == limit:
            result = sorted(result)
            word_list.append("".join(result))
            return

        for i in range(idx, length):
            menu_combi(length, i+1, cnt+1, limit, result+[order[i]])

    for number in course:
        word_list = []

        for order in orders:
            length = len(order)
            menu_combi(length, 0, 0, number, [])

        result = {}

        for word in word_list:
            result[word] = result.get(word, 0) + 1

        temp = []
        max_cnt = 2
        for key, value in result.items():
            if value > max_cnt:
                max_cnt = value
                temp = [key]
            elif value == max_cnt:
                temp.append(key)

        answer += temp

    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
