def solution(X, Y):
    answer = ""
    numbers_lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numbers_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
               "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    x_lst = [0] * 10
    y_lst = [0] * 10

    for i in range(9, -1, -1):

        x_lst[i] = X.count(numbers_lst[i])
        y_lst[i] = Y.count(numbers_lst[i])

    for i in range(9, -1, -1):

        if x_lst[i] > 0 and y_lst[i] > 0:

            count = min(x_lst[i], y_lst[i])
            answer += str(i) * count

    if answer == "":
        return "-1"

    if int(answer) == 0:
        return "0"

    return answer


def solution2(X, Y):
    answer = []
    numbers_lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(9, -1, -1):
        x_count, y_count = X.count(numbers_lst[i]), Y.count(numbers_lst[i])

        if x_count > 0 and y_count > 0:

            count = min(x_count, y_count)
            answer += [numbers_lst[i]] * count

    if not answer:
        return "-1"

    if answer.count("0") == len(answer):
        return "0"

    return "".join(answer)


print(solution2("100", "2345"))
print(solution2("100", "203045"))
