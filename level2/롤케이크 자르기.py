def solution(topping):
    answer = 0
    brother_dict = {}

    for element in topping:
        brother_dict[element] = brother_dict.get(element, 0) + 1

    standard = len(brother_dict.keys())
    target_dict = {}

    for element in topping:
        target_dict[element] = target_dict.get(element, 0) + 1
        count = len(target_dict.keys())

        if brother_dict[element] == target_dict[element]:
            standard -= 1

        if count == standard:
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))
