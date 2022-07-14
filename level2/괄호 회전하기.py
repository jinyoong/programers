def solution(s):
    answer = 0
    length = len(s)

    if length % 2:
        return answer

    new_s = s + s
    temp = {"[": -1, "]": 1, "{": -2, "}": 2, "(": -3, ")": 3}
    queue = [0 for _ in range(length * 2)]

    for i in range(2 * length - 1):

        queue[i + 1] = temp[new_s[i]]
        print(queue)

        if queue[i] == queue[i + 1] * -1 and queue[i] < queue[i + 1]:
            queue[i] = queue[i + 1] = 0

        if i + 1 >= length and queue[i + 2 - length:i + 2] == [0] * length:
            print(queue[i + 1 - length:i + 1])
            answer += 1

    return answer


def solution2(s):
    answer = 0
    length = len(s)

    if length % 2:
        return answer

    bracket_dict = {"(": 0, "[": 0, "{": 0}
    new_s = s + s

    for i in range(2 * length - 1):
        if i >= length and new_s[i - length] in {"(", "[", "{"} and bracket_dict[new_s[i - length]] >= 1:
            bracket_dict[new_s[i - length]] -= 1

        if new_s[i] in {"(", "[", "{"}:
            bracket_dict[new_s[i]] += 1

        else:
            if new_s[i] == ")" and bracket_dict["("] >= 1:
                bracket_dict["("] -= 1

            elif new_s[i] == "]" and bracket_dict["["] >= 1:
                bracket_dict["["] -= 1

            elif new_s[i] == "}" and bracket_dict["{"] >= 1:
                bracket_dict["{"] -= 1

        if i >= length - 1 and set(bracket_dict.values()) == {0, }:
            answer += 1

    return answer


def solution3(s):
    answer = 0
    length = len(s)
    new_s = s + s
    bracket_num = {"[": -1, "(": -2, "{": -3, "]": 1, ")": 2, "}": 3}

    if length % 2:
        return answer

    for start in range(length - 1):
        bracket_stack = [0]
        result = True

        for idx in range(length):
            i = start + idx

            if bracket_num[new_s[i]] <= -1:
                bracket_stack.append(bracket_num[new_s[i]])

            else:

                if bracket_stack[-1] == -1 * bracket_num[new_s[i]]:
                    bracket_stack.pop()

                else:
                    result = False
                    break

        if result and len(bracket_stack) == 1:
            answer += 1

    return answer


print(solution3("[](){}"))
print(solution3("}]()[{"))
print(solution3("[)(]"))
print(solution3("}}}"))
print(solution3("((()"))
