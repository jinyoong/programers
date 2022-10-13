def solution(survey, choices):
    answer = ''
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    character = ["RT", "CF", "JM", "AN"]
    total = {"T": 0, "R": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):

        choice = choices[i]
        first, second = survey[i]

        if choice >= 4:
            total[second] += score[choice]
        else:
            total[first] += score[choice]

    for i in range(4):
        left, right = character[i]

        if total[left] < total[right]:
            answer += right
        else:
            answer += left

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
