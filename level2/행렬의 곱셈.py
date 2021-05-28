def solution_2(arr1, arr2):
    answer = []
    # print('{} x {} 행렬이 만들어집니다.'.format(len(arr1), len(arr2[0])))
    for i in range(len(arr1)):
        first_list = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            first_list.append(temp)
        answer.append(first_list)
    return answer


print(solution_2([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution_2([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
print(solution_2([[1, 1], [2, 2]], [[1], [2]]))


def productMatrix(A, B):
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[1, 2], [2, 3]]
b = [[3, 4], [5, 6]]
print("결과 : {}".format(productMatrix(a, b)))
