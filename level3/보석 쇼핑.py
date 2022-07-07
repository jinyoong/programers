def solution(gems):
    answer = []
    answer_length = 987654321

    all_gems = set(gems)
    start = 0
    for i in range(len(gems)):
        end = i + 1

        if set(gems[start:end]) == all_gems:

            # temp = set()
            # front = start
            # while True:
            #     if set(gems[front:end]) == all_gems:
            #         if front in temp:
            #             start = front
            #             break
            #         temp.add(front)
            #         front = (end + front) // 2
            #     else:
            #         front //= 2

            # while True:
            #
            #     if gems[start] in gems[start + 1:end]:
            #         start += 1
            #     else:
            #         break

            idx = end - 1
            gem_set = set()
            while idx >= 0:
                gem_set.add(gems[idx])
                if gem_set == all_gems:
                    start = idx
                    break
                idx -= 1

            if answer_length > end - start:
                answer_length = end - start
                answer = [start + 1, end]

            start = i

    return answer


def solution2(gems):
    answer = [[0, 0], 987654321]
    all_gems = set(gems)
    gems = [""] + gems
    gem_dict = {}
    start = 1

    for i in range(1, len(gems)):
        gem = gems[i]
        end = i

        gem_dict[gem] = gem_dict.get(gem, 0) + 1

        if len(gem_dict) == len(all_gems):
            for j in range(start, end):
                gem = gems[j]
                if gem_dict[gem] == 1:
                    start = j
                    break
                else:
                    gem_dict[gem] -= 1

            if end - start < answer[1]:
                answer = [[start, end], end - start]

    return answer[0]


print(solution2(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution2(["XYZ", "XYZ", "XYZ"]))
