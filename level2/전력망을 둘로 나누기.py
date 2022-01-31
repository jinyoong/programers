def solution(n, wires):
    answer = 100

    tree_root_1 = [-1 for _ in range(n+1)]

    queue = [1] * n
    check = set()
    start = 0
    end = 1

    while start < end:
        node = queue[start]
        start += 1
        cnt = 0
        for ele in wires:
            n1, n2 = ele

            if n1 in check or n2 in check:
                continue

            if n1 == node:
                queue[end] = n2
                end += 1
                cnt += 1
                continue

            if n2 == node:
                queue[end] = n1
                end += 1
                cnt += 1
                continue

        check.add(node)
        tree_root_1[node] = cnt
        for parent in queue[:start-1]:

            if not tree_root_1[parent]:
                continue

            tree_root_1[parent] += cnt

    for child in tree_root_1[1:]:
        diff = abs(n - 2*(child+1))
        if answer > diff:
            answer = diff

    print(tree_root_1)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(9, [[1, 3], [4, 5], [8, 7], [9, 7], [7, 4], [4, 6], [3, 2], [4, 3]]))
print(solution(3, [[1, 2], [3, 2]]))
print(solution(8, [[1, 2], [1, 3], [1, 4], [4, 5], [5, 6], [6, 7], [6, 8]]))
