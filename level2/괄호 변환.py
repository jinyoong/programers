def solution(p):
    answer = ''
    is_fail = 0  # "("는 -1, ")"은 +1로 보고 올바른지 판단하자. 중간에 0보다 큰 수가 나오면 올바른 괄호라 할 수 없다.
    is_correct = True
    left_count = 0
    right_count = 0

    if p == "":
        return ""

    idx = 0
    for side in p:

        if side == "(":
            is_fail -= 1
            left_count += 1
        else:
            is_fail += 1
            right_count += 1

        if is_fail >= 1:
            is_correct = False

        if left_count == right_count and left_count >= 1:
            break

        idx += 1

    if idx == len(p):
        u = p
        v = ""
    else:
        u = p[:idx + 1]
        v = p[idx + 1:]

    if is_correct:
        answer += u + solution(v)

    else:
        reverse_str = ""
        for side in u[1:-1]:
            if side == "(":
                reverse_str += ")"
            else:
                reverse_str += "("

        answer += "(" + solution(v) + ")" + reverse_str

    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
