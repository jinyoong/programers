def solution(n, edge):

    temp = [[] for _ in range(n+1)]

    for ele in edge:
        n1, n2 = ele
        temp[n1].append(n2)
        temp[n2].append(n1)

    queue = [[1]]
    head = 0
    rear = 1
    visited = {1}

    while head < rear:
        nodes = queue[head]
        head += 1
        lst = []

        if nodes == []:
            break

        for node in nodes:
            for ele in temp[node]:
                if ele in visited:
                    continue
                visited.add(ele)
                lst.append(ele)

        queue.append(lst)
        rear += 1

    return len(queue[-2])


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))