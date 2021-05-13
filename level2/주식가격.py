def solution(prices):
    answer = [0 for i in prices]
    for i in range(len(prices)):
        print('{}인덱스의 주식 가격인 {}의 변동을 봅니다.'.format(i, prices[i]))
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                print('{}인덱스일 때 {}로 {}에 비해 가격이 떨어졌습니다.'.format(j, prices[j], prices[i]))
                answer[i] = j - i
                break
            elif j == len(prices) - 1:
                print('주식의 가격이 {}인덱스 이후로 떨어진 적이 없습니다.'.format(i))
                answer[i] = len(prices) - i - 1
    return answer


print(solution([1, 2, 3, 2, 3]))