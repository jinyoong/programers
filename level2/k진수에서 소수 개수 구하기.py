def solution(n, k):
    answer = 0
    numbers = {}

    if k == 10:
        number = str(n)
    else:
        number = number_to_k(n, k)

    zeros = []
    for i in range(len(number)):
        if number[i] == '0':
            zeros.append(i)

    zeros += [len(number)]

    start_idx = 0
    for idx in zeros:
        temp = number[start_idx:idx]
        start_idx = idx + 1

        if not temp:
            continue

        temp = int(temp)
        numbers[temp] = numbers.get(temp, 0) + 1

    for key, value in numbers.items():
        if is_prime(key):
            answer += value

    return answer


def number_to_k(n, k):
    result = ''

    while n >= k:
        n, y = divmod(n, k)
        result = str(y) + result

    if n != 0:
        result = str(n) + result

    return result


def is_prime(target):
    if target == 1:
        return False

    for t in range(2, int(target ** (1/2)) + 1):
        if target % t == 0:
            return False
    return True


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(2902900290002, 10))
print(solution(111, 10))
print(solution(1, 10))

