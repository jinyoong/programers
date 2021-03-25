def solution(s):
    answer = ''
    word_list = s.split(" ")
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            if(j%2 == 0):
                answer += word_list[i][j].upper()
            else:
                answer += word_list[i][j].lower()
        if(i != len(word_list)-1):
            answer += ' '
    return answer


print(solution("try hello world"))