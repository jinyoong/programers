def solution(brown, yellow):
    """
    b + r = x * y
    b = 2 * x + (y - 2) * 2
      = 2 * (x + y) - 4
    """
    area = brown+yellow
    answer = []
    for width in range(1, area+1):
        height = area / width

        if height % 1 or height > width:  # 세로의 길이가 자연수가 아니거나, 가로의 길이보다 더 긴 경우 다음으로
            continue

        if 2 * (width + height) - 4:
            answer.append([width, int(height)])
            break

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
