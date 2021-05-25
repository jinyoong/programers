def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        if (num ** 0.5) % 1 != 0:
            # print('{}은 약수의 개수가 짝수개 입니다.'.format(num))
            answer += num
        else:
            # print('{}은 약수의 개수가 홀수개 입니다.'.format(num))
            answer -= num
    return answer

print(solution(13, 17))