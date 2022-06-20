def num_push(queue, x, y):
    idx = len(queue)
    queue.append([x, y])

    while idx > 1:
        if queue[idx // 2][0] < queue[idx][0]:
            queue[idx // 2][0], queue[idx][0] = queue[idx][0], queue[idx // 2][0]
            idx //= 2

        if queue[idx // 2][1] > queue[idx][1]:
            queue[idx // 2][1], queue[idx][1] = queue[idx][1], queue[idx // 2][1]
            idx // 2

        if queue[idx // 2][0] >= queue[idx][0] and queue[idx // 2][1] <= queue[idx][1]:
            break


def solution(operations):
    answer = []

    queue = [[0, 0]]
    for ele in operations:
        if ele[0] == 'I':
            num_push(queue, int(ele[2:]), int(ele[2:]))

    return queue


print(solution(["I 7","I 5","I -5","D -1"]))
