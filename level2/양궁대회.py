def solution(n, info):
    """
    어피치가 i 점에 k 발을 맞췄다면, 라이언이 할 수 있는 선택지는 k+1 발을 맞추거나, 0 발을 맞추는 것
    그 이상 맞추거나 사이를 맞추면 무조건 손해
    """
    answer = [0] * 11
    answer_list = [0, answer]

    def competition(idx, cnt, score):
        nonlocal answer_list

        if cnt == 0:
            diff = calculate(info, score)
            if diff > answer_list[0]:
                answer_list = [diff, score[:]]
            elif diff == answer_list[0]:
                # 차이가 같으면 더 낮은 점수를 더 많이 맞힌 경우를 채택한다
                for i in range(10, -1, -1):
                    if score[i] > answer_list[1][i]:
                        answer_list[1] = score[:]
                        break
                    elif score[i] < answer_list[1][i]:
                        break
            return

        if idx == 10 and cnt > 0:
            score[idx] = cnt
            competition(idx + 1, 0, score)
            score[idx] = 0
        else:
            if info[idx] + 1 <= cnt:
                temp = info[idx] + 1
                score[idx] = temp
                competition(idx + 1, cnt - temp, score)
                score[idx] = 0

            competition(idx + 1, cnt, score)

    competition(0, n, answer)

    if answer_list[0]:
        return answer_list[1]
    else:
        return [-1]


def calculate(peach, lion):
    peach_score = lion_score = 0
    for i in range(11):
        if peach[i] == lion[i] == 0:
            continue

        if peach[i] >= lion[i]:
            peach_score += 10-i
        else:
            lion_score += 10-i

    if peach_score < lion_score:
        return lion_score - peach_score
    else:
        return 0


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(5, [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
