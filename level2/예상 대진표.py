def solution(n,a,b):
    print('------------------------------------------------------------')
    answer = 1

    if a > b:
        a, b = b, a

    while True:
        if b % 2 == 0 and a + 1 == b:
            break
        print('A : {}, B : {}'.format(a, b))
        if a % 2 == 0:
            a = int(a / 2)
        else:
            a = int(a / 2) + 1
        if b % 2 == 0:
            b = int(b / 2)
        else:
            b = int(b / 2) + 1
        answer += 1

    print('A : {}, B : {}'.format(a, b))
    return answer

print(solution(8, 4, 7))
print(solution(17, 16, 4))
print(solution(40, 2, 33))
print(solution(150, 7, 97))
print(solution(3, 1, 2))
print(solution(3, 2, 3))