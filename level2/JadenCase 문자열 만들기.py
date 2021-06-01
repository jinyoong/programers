def solution(s):
    answer = ''

    s = s.split(' ')
    print(s)
    for i in s:
        if i == '':
            answer = answer + ' '
            continue
        if i[0].isdigit():
            a = i[0]
        else:
            a = i[0].upper()
        b = i[1:].lower()
        answer = answer + a + b + " "

    return answer[:-1]

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution('a b c d ed f easg sdgacvsd dsgawe'))
print(solution(' 3 2 1 zero i am  k ing '))