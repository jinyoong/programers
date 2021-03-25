def solution(n):
    answer = 0
    rev = []
    new_num = ''
    for num in str(n):
        rev.append(num)
    rev.sort(reverse=True)
    for i in range(len(rev)):
        new_num += rev[i]
    answer = int(new_num)
    return answer

#다른 사람 풀이
def solution2(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

print(solution(12345))