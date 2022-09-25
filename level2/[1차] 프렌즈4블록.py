def solution(m, n, board):
    answer = 0
    delete_set = set()
    is_delete = True
    new_board = [[""] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            new_board[r][c] = board[r][c]

    while is_delete:

        for r in range(m - 1):
            for c in range(n - 1):

                if not new_board[r][c]:
                    continue

                standard = new_board[r][c]
                can_delete = set()

                for i in range(2):
                    for j in range(2):
                        nr, nc = r + i, c + j
                        adj_block = new_board[nr][nc]

                        if adj_block == standard:
                            can_delete.add((nr, nc))

                if len(can_delete) == 4:
                    delete_set = delete_set.union(can_delete)

        if not delete_set:
            is_delete = False
            continue

        update_board = [[""] * n for _ in range(m)]

        for c in range(n):
            r_idx = m - 1
            for r in range(m - 1, -1, -1):

                if (r, c) not in delete_set:
                    update_board[r_idx][c] = new_board[r][c]
                    r_idx -= 1

        answer += len(delete_set)
        delete_set = set()
        new_board = update_board

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
