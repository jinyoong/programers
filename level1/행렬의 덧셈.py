def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        if(len(arr1[i]) >= 2):
            small_list = []
            for j in range(len(arr1[i])):
                small_list += [arr1[i][j]+arr2[i][j]]
            answer += [small_list]
        else:
            answer += [[arr1[i][0] + arr2[i][0]]]
    return answer

print(solution([[1,2], [2,3]], [[3,4], [4,5]]))
print(solution([[1],[2]],[[3],[4]]))