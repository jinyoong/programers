def solution(babbling):
    answer = 0
    word_set_1 = {"ye", "ma"}
    word_set_2 = {"aya", "woo"}

    for babbling_ele in babbling:
        temp = ""
        before = ""
        for alpha in babbling_ele:

            temp += alpha

            if len(temp) == 2 and temp in word_set_1 and temp != before:
                before = temp
                temp = ""
                continue

            if len(temp) == 3 and temp in word_set_2 and temp != before:
                before = temp
                temp = ""
                continue

            if len(temp) == 1:
                continue

            if len(temp) == 3:
                break

        if not temp:
            answer += 1

    return answer


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

