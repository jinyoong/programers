def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))]

    for edge in edges:
        parent, child = edge
        tree[parent].append(child)

    def collect(possible, sheep, wolf):
        nonlocal answer

        if sheep > answer:
            answer = sheep

        for current_node in possible:  # 이미 다녀온 노드들 중 출발지를 정하기 위한 반복문

            for next_node in tree[current_node]:  # 출발지로 정한 노드의 자식 노드들을 살피기 위한 반복문

                if next_node in possible:  # 만약 자식 노드가 이미 다녀온 노드들 중 하나로 있다면, 더 볼 필요가 없다
                    continue

                if info[next_node] and sheep - 1 == wolf:  # 다음으로 늑대를 가져가면 양이 다 잡아먹히는 경우
                    continue

                possible.add(next_node)  # 자식 노드를 다녀온 노드에 추가한다

                if info[next_node]:  # 다음이 늑대인 경우
                    collect(possible, sheep, wolf + 1)
                else:  # 다음이 양인 경우
                    collect(possible, sheep + 1, wolf)

                possible.remove(next_node)  # 자식 노드를 다녀온 노드에서 제거한다

    collect({0}, 1, 0)

    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
