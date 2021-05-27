def solution(citations):
    answer = 0
    for i in range(max(citations)):
        quotation_ct = 0
        not_quotation_ct = 0
        equal_ct = 0
        for num in citations:
            if num > i:
                quotation_ct += 1
            elif num < i:
                not_quotation_ct += 1
            else:
                equal_ct += 1
        # print('{}번 보다 많이 인용된 논문이 {}개 입니다.'.format(i, quotation_ct))
        # print('{}번 적게 많이 인용된 논문이 {}개 입니다.'.format(i, not_quotation_ct))
        # print('{}번 인용된 논문이 {}개 입니다.'.format(i, equal_ct))
        if quotation_ct >= i:
            answer = i
        elif quotation_ct + equal_ct >= i:
            answer = i
    return answer

print(solution([3, 0, 6, 1, 5]))
print(solution([3, 3, 6, 1, 5]))

# 다른 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0