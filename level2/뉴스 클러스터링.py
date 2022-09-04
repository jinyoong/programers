def solution(str1, str2):
    dict1 = {}
    dict2 = {}

    for j in range(2):
        ele_str, ele_dict = [str1, dict1] if j == 0 else [str2, dict2]
        for i in range(1, len(ele_str)):
            temp = ele_str[i-1:i+1].lower()

            if not temp.isalpha():
                continue

            ele_dict[temp] = ele_dict.get(temp, 0) + 1

    dict1_set = set(dict1.keys())
    dict2_set = set(dict2.keys())

    numerator = dict1_set.intersection(dict2_set)
    denominator = dict1_set.union(dict2_set)

    if not denominator:
        return 65536

    numerator_cnt = 0
    for ele in numerator:
        numerator_cnt += min(dict1[ele], dict2[ele])

    denominator_cnt = 0
    for ele in denominator:
        denominator_cnt += max(dict1.get(ele, 0), dict2.get(ele, 0))

    answer = (numerator_cnt / denominator_cnt) * 65536

    return int(answer)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
