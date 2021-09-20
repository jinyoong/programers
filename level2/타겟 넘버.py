operation = ['+', '-']
answer = 0


def ans_def(idx, numbers, num_sum, target):
    global answer

    if idx == len(numbers):
        if num_sum == target:
            answer += 1
        return

    ans_def(idx+1, numbers, num_sum+numbers[idx], target)
    ans_def(idx+1, numbers, num_sum-numbers[idx], target)

    return answer


def solution(numbers, target):
    result = ans_def(0, numbers, 0, target)
    return result


print(solution([1, 1, 1, 1, 1], 3))
