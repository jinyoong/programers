def solution(n, k, cmd):
    answer = ''
    lst = [0 for _ in range(n)]
    check = []
    lst[k] = 1

    for order in cmd:
        if order[0] == "U":
            step = int(order[2])
            count = 1
            while step > 0:
                if lst[k - count] != -1:
                    step -= 1
                count += 1
            lst[k] = 0
            k -= count - 1
            lst[k] = 1

        elif order[0] == "D":
            step = int(order[2])
            count = 1
            while step > 0:
                if lst[k + count] != -1:
                    step -= 1
                count += 1
            lst[k] = 0
            k += count - 1
            lst[k] = 1

        elif order[0] == "C":
            lst[k] = -1
            check.append(k)

            if k == n - 1:
                for i in range(n - 1, -1, -1):
                    if lst[i] == 0:
                        lst[i] = 1
                        k = i
                        break

            else:
                for i in range(k + 1, n):
                    if lst[i] == 0:
                        lst[i] = 1
                        k = i
                        break

        else:
            point = check.pop()
            lst[point] = 0

    for num in lst:
        if num == -1:
            answer += "X"
        else:
            answer += "O"

    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
