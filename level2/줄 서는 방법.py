def solution(n, k):
    """
    1 2 3 4 5
    1 2 3 5 4
    1 2 4 3 5
    1 2 4 5 3
    1 2 5 3 4
    1 2 5 4 3
    1 3 2 4 5
    1 3 2 5 4
    1 3 4 2 5
    1 3 4 5 2
    1 3 5 2 4
    1 3 5 4 2

    우리가 k 번째 수가 필요한 경우, 그 전 숫자들은 총 k - 1개가 존재한다.

    5번째 숫자 배열을 찾는다고 하자.
    앞에는 4개의 숫자 배열이 존재한다.

    5번째 숫자 배열은 1 2 5 3 4 이다.
    만의 자리를 고정했을 때 나오는 경우의 수 : 24가지
    즉, 만의 자리는 바뀌면 안된다.

    천의 자리를 고정했을 때 나오는 경우의 수 : 6가지
    즉, 천의 자리는 바뀌면 안된다.

    백의 자리를 고정했을 때 나오는 경우의 수 : 2가지
    즉, 백의 자리는 2번 바뀐다.

    10번째 숫자 배열은 1 3 4 5 2 이다.
    만의 자리를 고정한 경우 : 24가지
    즉, 만의 자리는 바뀌면 안된다.
    1

    천의 자리를 고정한 경우 : 6가지
    즉, 천의 자리는 한 번 바뀐다.
    1 3

    백의 자리를 고정한 경우 : 2가지
    즉, 백의 자리는 1번 바뀐다.
    1 3 4

    십의 자리를 고정한 경우 : 1가지
    즉, 십의 자리는 1번 바뀐다.
    1 3 4 5 2
    """
    answer = []
    count = 1

    for i in range(1, n):
        count *= i

    number_lst = [i for i in range(1, n + 1)]
    before = k - 1
    standard = n

    while len(answer) < n:
        idx = 0 if count == 0 else (before // count) % len(number_lst)
        number = number_lst.pop(idx)

        if count:
            before %= count

        answer.append(number)
        standard -= 1

        if standard:
            count //= standard

    return answer


print(solution(3, 5))
print(solution(3, 2))
print(solution(1, 1))
print(solution(5, 5))
