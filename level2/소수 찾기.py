def is_prime(num):
    if num == 1:
        return False

    for i in range(2, round(num)):
        if num % i == 0:
            return False

    return True


def solution(numbers):

    answer = 0
    if '2' in numbers:
        answer = 1
    num_lst = []

    def make_num(numbers, idx, N, temp):
        nonlocal answer

        if idx == N:
            if int(temp) not in num_lst and is_prime(int(temp)):
                answer += 1
                num_lst.append(int(temp))
            return

        for j in range(len(numbers)):

            if used[j]:
                continue

            if not temp and numbers[j] == '0':
                continue

            if not temp and not int(numbers[j]) % 2:
                continue

            used[j] = True
            make_num(numbers, idx+1, N, numbers[j]+temp)
            used[j] = False

    N = len(numbers)

    for i in range(1, N+1):
        used = [False] * N
        make_num(numbers, 0, i, '')

    return answer


print(solution('17'))
print(solution('011'))