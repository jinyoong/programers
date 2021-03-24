def solution(a, b):
    dot_pd = 0
    for i in range(len(a)):
        dot_pd += a[i]*b[i]
    return dot_pd

print(solution([1,2,3,4],[-3,-1,0,2]))