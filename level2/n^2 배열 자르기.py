def solution(n, left, right):
    answer = [0] * (right - left + 1)
    # temp = [0] * (n ** 2)
    #
    # for r in range(n):
    #     for c in range(n):
    #         num = max(r, c) + 1
    #         temp[r * n + c] = num

    # numbers = [i+1 for i in range(n)]
    # temp = numbers[:]
    #
    # for i in range(1, n):
    #     for j in range(i):
    #         numbers[j] = i+1
    #     temp += numbers
    #
    # for i in range(left, right+1):
    #     answer[i-left] = temp[i]

    for i in range(left, right+1):
        x, y = divmod(i, n)
        num = x + 1
        if y > x:
            num = y + 1

        answer[i-left] = num

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
