def solution(rows, columns, queries):
    answer = []

    numbers = [[0] * columns for _ in range(rows)]

    number = 1
    for r in range(rows):
        for c in range(columns):
            numbers[r][c] = number
            number += 1

    print(numbers)

    for querie in queries:
        sr, sc, fr, fc = querie
        current = numbers[sr-1][sc-1]
        result = current

        for nc in range(sc, fc):
            temp = numbers[sr-1][nc]
            numbers[sr-1][nc] = current
            current = temp
            if result > current:
                result = current

        for nr in range(sr, fr):
            temp = numbers[nr][fc-1]
            numbers[nr][fc-1] = current
            current = temp
            if result > current:
                result = current

        for nc in range(fc-2, sc-2, -1):
            temp = numbers[fr - 1][nc]
            numbers[fr - 1][nc] = current
            current = temp
            if result > current:
                result = current

        for nr in range(fr-2, sr-2, -1):
            temp = numbers[nr][sc - 1]
            numbers[nr][sc - 1] = current
            current = temp
            if result > current:
                result = current

        answer.append(result)

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
