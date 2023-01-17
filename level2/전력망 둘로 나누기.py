def solution(n, wires):
    answer = 100
    tree = [[0] * (n + 1) for _ in range(n + 1)]

    for node1, node2 in wires:
        tree[node1][node2] = 1
        tree[node2][node1] = 1

    for node1, node2 in wires:
        tree[node1][node2] = 0
        tree[node2][node1] = 0

        count_node1 = count_node(node1, tree)
        count_node2 = count_node(node2, tree)

        if answer > abs(count_node1 - count_node2):
            answer = abs(count_node1 - count_node2)

        tree[node1][node2] = 1
        tree[node2][node1] = 1

    return answer


def count_node(target, sub_tree):

    queue = [target]
    visited = {target, }
    idx = 0
    length = 1

    while idx < length:
        current = queue[idx]
        idx += 1

        for adj_node, value in enumerate(sub_tree[current]):

            if value == 0:
                continue

            if adj_node in visited:
                continue

            queue.append(adj_node)
            visited.add(adj_node)
            length += 1

    return len(visited)


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
