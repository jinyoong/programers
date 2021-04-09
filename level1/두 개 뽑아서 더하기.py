def solution(numbers):
    a = len(numbers)
    answer = []
    numbers.sort(reverse = True)
    for i in range(a):
        for j in range(a):
            if(i!=j):
                answer.append(numbers[i]+numbers[j])
    answer = set(answer)
    answer = list(answer)
    answer.sort(reverse = False)
    return answer

print(solution([2,1,3,4,1]))