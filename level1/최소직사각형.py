def solution(sizes):

    max_left = 0
    max_right = 0

    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]

        if max_left < size[0]:
            max_left = size[0]

        if max_right < size[1]:
            max_right = size[1]

    answer = max_left * max_right

    return answer
