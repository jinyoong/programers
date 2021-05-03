def solution(lottos, win_nums):
    answer = []
    temp = [6, 5, 4, 3, 2]

    # 먼저 알 수 없는 번호들의 개수를 구한다.
    zero_ct = lottos.count(0)

    # 민우가 확인한 번호와 당첨번호 중 같은 번호의 개수를 구한다.
    equal_ct = len(set(lottos) & set(win_nums))

    # 0의 개수만큼 더한 값이 최고 등수이다.
    if equal_ct + zero_ct in temp:
        answer.append(temp.index(equal_ct + zero_ct) + 1)
    else:
        answer.append(6)

    # 최저 순위는 equall_ct의 개수로 순위를 매길 때이다.
    if equal_ct in temp:
        answer.append(temp.index(equal_ct) + 1)
    else:
        answer.append(6)
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))