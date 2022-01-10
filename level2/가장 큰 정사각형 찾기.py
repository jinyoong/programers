def solution(board):
    answer = 0
    len_row = len(board)
    len_col = len(board[0])

    for r in range(len_row):
        for c in range(len_col):
            if not answer and board[r][c]:
                answer = 1

            if r == 0 or c == 0:
                continue

            if not board[r][c]:
                continue

            board[r][c] = min(board[r-1][c-1], board[r-1][c], board[r][c-1]) + 1
            if answer < board[r][c]:
                answer = board[r][c]

    return answer * answer


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[0,0,1,1],[0,0,1,1],[0,0,1,0]]))
print(solution([[0,0,1,0],[0,0,1,1],[0,0,1,1],[0,0,1,0]]))
print(solution([[0,1,0,1],[0,1,0,1],[0,1,1,1],[0,0,0,0]]))

"""
0 0 1 1
0 0 1 1
0 0 1 1
0 0 1 0
답 : 4

0 0 1 0
0 0 1 1
0 0 1 1
0 0 1 0
답 : 4

0 1 0 1
0 1 0 1
0 1 1 1
0 0 0 0
답 : 1
"""