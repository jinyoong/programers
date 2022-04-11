def solution(n):
    answer = ''
    x = n

    while x > 2:
        x, y = divmod(x, 3)
        if y == 0:
            x = x - 1
            answer += str(4)
        else:
            answer += str(y)
    if x != 0:
        answer += str(x)

    return answer[::-1]
