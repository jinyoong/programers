#재귀함수, 메모이제이션 사용
'''dic_fibo = {0: 0, 1: 1}
def solution(n):
    answer = 0
    if n in dic_fibo.keys():
        return dic_fibo[n]
    else:
        dic_fibo[n] = solution(n - 1) + solution(n - 2)
        return dic_fibo[n]%1234567'''



def solution_2(n):
    answer = 0
    fibo_list = [0,1]
    for i in range(n-1):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])
    return fibo_list[-1]%1234567



print(solution_2(5))
