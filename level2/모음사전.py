def solution(word):
    result = []
    alpha_dict = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4, "N": 5}
    alpha_list = ["A", "E", "I", "O", "U", "N"]
    answer = 0

    while True:
        answer += 1

        if len(result) == 5:
            result[-1] = alpha_list[(alpha_dict[result[-1]] + 1) % 6]

        else:
            result += ["A"]

        while "N" in result:
            if alpha_dict[result[-1]] == 5:
                result[-2] = alpha_list[(alpha_dict[result[-2]] + 1) % 6]
                result.pop(-1)

        if "".join(result) == word:
            return answer


print(solution("EIO"))
