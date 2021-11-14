def solution(places):
    answer = []

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for place in places:

        p_index = []
        result = 1

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_index.append([i, j])

        if not p_index:
            answer.append(1)
            continue

        first_stop = False

        for p in p_index:
            row, col = p

            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]

                if new_row < 0 or new_row >= 5 or new_col < 0 or new_col >= 5:
                    continue

                if place[new_row][new_col] == 'P':
                    first_stop = True
                    result = 0
                    break

                if place[new_row][new_col] == 'X':
                    continue

                second_stop = False

                for j in range(4):
                    over_row = new_row + dr[j]
                    over_col = new_col + dc[j]

                    if over_row == row and over_col == col:
                        continue

                    if over_row < 0 or over_row >= 5 or over_col < 0 or over_col >= 5:
                        continue

                    if place[over_row][over_col] == 'P':
                        second_stop = True
                        result = 0
                        break

                if second_stop:
                    break

            if first_stop:
                break

        answer.append(result)

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
