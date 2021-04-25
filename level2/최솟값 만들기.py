def solution(A,B):
    answer = 0
    A.sort(reverse=False)
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer

print(solution([1,4,2], [5,4,4]))