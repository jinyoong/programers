def solution(n, computers):
    answer = 0

    number = [0 for _ in range(n)]

    for i in range(n):
        if number[i]:
            continue

        check = {i, }
        queue = [i]
        head = 0
        rear = 1

        while head < rear:
            current = queue[head]
            head += 1

            if number[current]:
                break

            number[current] = 1

            computer = computers[current]
            for next_node, line in enumerate(computer):
                if not line:
                    continue

                if next_node in check:
                    continue

                queue.append(next_node)
                check.add(next_node)
                rear += 1

        answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
