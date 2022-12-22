def solution(n, costs):
    answer = 0
    sorted_costs = sorted(costs, key=lambda x: x[2])
    parents = [i for i in range(n)]
    count = 0

    for cost in sorted_costs:
        node1, node2, line = cost
        parent_node1 = find_parent(parents, node1)
        parent_node2 = find_parent(parents, node2)

        if parent_node1 == parent_node2:
            continue

        answer += line
        count += 1

        if parent_node1 < parent_node2:
            parents[parent_node2] = parent_node1
        else:
            parents[parent_node1] = parent_node2

        if count == n - 1:
            break

    return answer


def find_parent(parents, child):
    parent = parents[child]

    if parent == child:
        return parent

    return find_parent(parents, parent)


print(solution(1, []))
print(solution(2, [[0, 1, 1]]))
print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(solution(4, [[0, 1, 1], [0, 2, 2], [2, 3, 1]]))
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))
