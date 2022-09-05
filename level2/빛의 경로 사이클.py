def solution(grid):
    answer = []
    col_len = len(grid[0])
    row_len = len(grid)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    answer_check = []

    for i in range(4):
        br = bc = 0
        idx = i
        check = set()

        while True:

            if grid[br][bc] == "S":
                nr, nc = br + dr[idx], bc + dc[idx]

            elif grid[br][bc] == "R":
                nr, nc = br + dr[(idx + 1) % 4], bc + dc[(idx + 1) % 4]
                idx = (idx + 1) % 4

            else:
                nr, nc = br + dr[(idx + 3) % 4], bc + dc[(idx + 3) % 4]
                idx = (idx + 3) % 4

            fr, fc = nr, nc

            if nr < 0:
                nr = row_len - 1

            if nr >= row_len:
                nr = 0

            if nc < 0:
                nc = col_len - 1

            if nc >= col_len:
                nc = 0

            if (br, bc, fr, fc) in check:
                print(check)
                if check not in answer_check:
                    answer.append(len(check))
                    answer_check.append(check)
                break

            check.add((br, bc, fr, fc))
            # print("출발 좌표 : ({} {}), 도착 좌표 : ({} {})".format(br, bc, nr, nc))
            # print((br, bc, fr, fc))

            br, bc = nr, nc

    answer.sort()
    return answer


print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))
