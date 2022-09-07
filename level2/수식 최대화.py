def solution(expression):
    answer = 0
    c = ['+', '-', '*']


    calc = []
    calc_per = []

    temp_s = ''
    num = []

    for s in expression:

        if s in c:
            num.append(int(temp_s))
            temp_s = ''
            num.append(s)
            calc.append(s)
        else:
            temp_s += s

    num.append(int(temp_s))
    calc = list(set(calc))

    for i in range(len(calc)):
        temp = [calc[i]]
        if len(temp) != len(calc):
            for j in range(len(calc)):
                if calc[j] == calc[i]:
                    pass
                else:
                    temp = [calc[i], calc[j]]
                    if len(temp) == len(calc):
                        calc_per.append(temp)
                        break
                    else:
                        l = set(calc) - set(temp)
                        temp += list(l)
                        calc_per.append(temp)
        else:
            calc_per.append(temp)

    # print(calc_per)

    for c in calc_per:
        # print()
        # print('우선순위가 {}인 연산을 진행합니다.'.format(c))
        num_temp = num.copy()
        for k in range(len(c)):
            # print('{}연산을 진행합니다.'.format(c[k]))
            # print('현재 연산해야 할 식은 {}입니다.'.format(num_temp))
            n = 1
            while len(num_temp) != 1:

                if num_temp[n] == c[k]:
                    if c[k] == '+':
                        t = num_temp[n - 1] + num_temp[n + 1]
                    elif c[k] == '*':
                        t = num_temp[n - 1] * num_temp[n + 1]
                    else:
                        t = num_temp[n - 1] - num_temp[n + 1]

                    del num_temp[n - 1: n + 2]
                    num_temp.insert(n - 1, t)
                    # print(num_temp)
                    n = 1
                else:
                    n += 2
                    if n >= len(num_temp):
                        break
        # print(abs(num_temp[0]))
        if answer < abs(num_temp[0]):
            answer = abs(num_temp[0])

    return answer

# 위에 푼 코드가 예전 코드라서 아래 코드로 바꾸는 중!!

# def solution(expression):
#     answer = 0
#     default_operator = ['+', '-', '*']
#     operator = []
#     num = []
#
#     temp_num = ""
#     for s in expression:
#
#         if s in default_operator:
#             num += [int(temp_num), s]
#             temp_num = ''
#             operator += [s] if s not in operator else []
#         else:
#             temp_num += s
#
#     num.append(int(temp_num))
#     operator_permutation = []
#
#     def permutation(cnt, result):
#         nonlocal operator_permutation
#
#         if cnt == len(operator):
#             operator_permutation.append(result)
#             return
#
#         for ele in operator:
#             if ele in result:
#                 continue
#             permutation(cnt + 1, result + [ele])
#
#     permutation(0, [])
#     print(operator_permutation)
#
#     for operator_per_ele in operator_permutation:
#
#         num_temp = [0] * len(num)
#         result = 0
#         while num_temp == [1] * len(num):
#             for operator_ele in operator_per_ele:
#
#
#     return answer
#
#
# print(solution("100-200*300-500+20"))
