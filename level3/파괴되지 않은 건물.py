def solution(board, skill):
    answer = len(board) * len(board[0])
    type_lst = [0, -1, 1]

    for ele in skill:
        skill_type, sr, sc, fr, fc, weight = ele
        for r in range(sr, fr + 1):
            for c in range(sc, fc + 1):
                before = board[r][c]
                board[r][c] += type_lst[skill_type] * weight

                if before >= 1 and board[r][c] <= 0 and skill_type == 1:
                    answer -= 1

                if before <= 0 and board[r][c] >= 1 and skill_type == 2:
                    answer += 1

    return answer


def solution2(board, skill):
    answer = 0
    type_lst = [0, -1, 1]
    change_map = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for ele in skill:
        skill_type, sr, sc, fr, fc, weight = ele
        change_map[sr][sc] += type_lst[skill_type] * weight
        change_map[sr][fc + 1] += type_lst[skill_type] * -1 * weight
        change_map[fr + 1][sc] += type_lst[skill_type] * - 1 * weight
        change_map[fr + 1][fc + 1] += type_lst[skill_type] * weight

    for r in range(len(board) + 1):
        for c in range(len(board[0])):
            change_map[r][c + 1] += change_map[r][c]

    for c in range(len(board[0]) + 1):
        for r in range(len(board)):
            change_map[r + 1][c] += change_map[r][c]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if change_map[r][c] + board[r][c] >= 1:
                answer += 1

    return answer


print(solution2([[5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4],
                [1, 2, 0, 2, 3, 2],
                [2, 1, 0, 3, 1, 2],
                [1, 0, 1, 3, 3, 1]]))
print(solution2([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],
               [[1, 1, 1, 2, 2, 4],
                [1, 0, 0, 1, 1, 2],
                [2, 2, 0, 2, 0, 100]]))
