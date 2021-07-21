def solution(s):
    alpha_num_dict = {'zero': 0,
                      'one': 1,
                      'two': 2,
                      'three': 3,
                      'four': 4,
                      'five': 5,
                      'six': 6,
                      'seven': 7,
                      'eight': 8,
                      'nine': 9 }
    answer = ''
    temp = ''
    for i in range(len(s)):
        if s[i].isalpha():
            temp += s[i]
            try:
                alpha_num_dict[temp]
            except:
                continue
            else:
                answer += str(alpha_num_dict[temp])
                temp = ''
        else:
            answer += str(s[i])
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))