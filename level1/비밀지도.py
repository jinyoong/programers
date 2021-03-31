def solution(n, arr1, arr2):
    answer = []
    b_1 = []
    b_2 = []
    for i in range(n):
        a = arr1[i]
        b = ''
        while(a > 0):
            x, y = divmod(a, 2)
            a = x
            b = str(y) + b
        while(len(b) < n):
            b = '0' + b
        b_1 += [b]
    for j in range(n):
        a = arr2[j]
        b = ''
        while(a > 0):
            x, y = divmod(a, 2)
            a = x
            b = str(y) + b
        while(len(b) < n):
            b = '0' + b
        b_2 += [b]
    print(b_1)
    print(b_2)
    for k in range(n):
        road = ''
        for m in range(n):
            if(int(b_1[k][m]) or int(b_2[k][m])):
                road += '#'
            else:
                road += ' '
        answer += [road]
    return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))