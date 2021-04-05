def solution(d, budget):
    answer = 0
    d_sum = 0
    d.sort(reverse=False)
    for i in d:
        if(d_sum + i <= budget):
            answer += 1
            d_sum += i
        else:
            break
    return answer


print(solution([1,3,2,5,4], 9))