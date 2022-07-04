idx_lst = []


def collection(number, result):
    global idx_lst

    if len(result) == number:
        idx_lst.append(result)
        return

    for i in range(number):
        if i in result:
            continue
        collection(number, result + [i])


def solution(k, dungeons):
    answer = -1
    collection(len(dungeons), [])

    for idx in idx_lst:
        result = 0
        temp_k = k
        print(idx)
        for i in idx:
            if dungeons[i][0] > temp_k:
                if result > answer:
                    answer = result
                break

            temp_k -= dungeons[i][1]
            result += 1

        if result > answer:
            answer = result

        if result == len(dungeons):
            return len(dungeons)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
