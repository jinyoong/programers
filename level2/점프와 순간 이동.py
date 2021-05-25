def solution(n):
    ans = 0
    while n != 0:
        print("\n{}에 도달하기 위해 어떻게 이동해야 하는지 역추적합니다.".format(n))
        if n % 2 == 1:
            print('{}에서 한 칸 앞으로 점프해 {}로 이동했습니다.'.format(n-1, n))
            n -= 1
            ans += 1
            print('지금까지 총 점프 수는 {}입니다.'.format(ans))
        else:
            print('{}에서 순간 이동하여 {}로 이동했습니다.'.format(int(n/2), n))
            n = int(n/2)
    return ans

print(solution(5))
print(solution(6))
print(solution(5000))


# 다른 사람 풀이
def solution2(n):
    return bin(n).count('1')