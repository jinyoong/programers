def solution(arr):
    answer = [0, 0]

    def check(sr, sc, length):
        standard = arr[sr][sc]

        for i in range(length):
            for j in range(length):

                if standard != arr[sr + i][sc + j]:
                    return False

        return True

    def recursion(sr, sc, n):
        number = arr[sr][sc]

        if n == 1:
            answer[number] += 1
            return

        if check(sr, sc, n):
            answer[number] += 1
            return

        for dr, dc in [[0, 0], [0, n//2], [n//2, 0], [n//2, n//2]]:
            nr, nc = sr + dr, sc + dc

            recursion(nr, nc, n//2)

    recursion(0, 0, len(arr))

    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
