def solution(s):
    answer = ''
    #문자열을 공백을 기준으로 나누어 리스트로 만듦
    s_list = list(map(int, s.split(" ")))
    min_num = s_list[0]
    max_num = s_list[0]
    for i in range(1, len(s_list)):
        if min_num >= s_list[i]:
            min_num = s_list[i]
        if max_num <= s_list[i]:
            max_num = s_list[i]
    answer = str(min_num) + " " + str(max_num)
    return answer

print(solution('-1 -1'))