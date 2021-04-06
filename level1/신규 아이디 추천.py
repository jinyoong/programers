def solution(new_id):
    answer = ''
    temp = ''
    #1. 대문자를 소문자로 변경
    new_id = new_id.lower()
    print('1번째 작업 후 {}'.format(new_id))
    #2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for i in new_id:
        if(97<=ord(i)<=122 or i.isdigit() == True or i == '_' or i == '-' or i == '.'):
            temp += i
            new_id = temp
    print('2번째 작업 후 {}'.format(new_id))
    #3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    temp_2 = ''
    for j in range(len(new_id)):
        if(j < len(new_id) - 1 and (new_id[j] == '.' and new_id[j+1] == '.')):
            temp_2 += ''
        else:
            temp_2 += new_id[j]
    print('3번째 작업 후 {}'.format(temp_2))
    #4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    if(temp_2[0] == '.'):
        if(len(temp_2) == 1):
            temp_2 = ''
        else:
            temp_2 = temp_2[1:]
    if(len(temp_2) >= 1):
        if(temp_2[-1] ==  '.'):
            if(len(temp_2) == 1):
                temp_2 = ''
            else:
                temp_2 = temp_2[:-1]
    print('4번째 작업 후 {}'.format(temp_2))
    #5. 빈 문자열이라면, new_id에 "a"를 대입
    if(temp_2 == ''):
        temp_2 += 'a'
    print('5번째 작업 후 {}'.format(temp_2))
    #6. 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if(len(temp_2) >= 16 and temp_2[14] == '.'):
        temp_2 = temp_2[:14]
    elif(len(temp_2) >= 16):
        temp_2 = temp_2[:15]
    print('6번째 작업 후 {}'.format(temp_2))
    #7. 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while(len(temp_2) < 3):
        temp_2 += temp_2[-1]
    print('7번째 작업 후 {}'.format(temp_2))
    answer = temp_2
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm12345"))