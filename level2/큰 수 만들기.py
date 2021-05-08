def solution(number, k):
    answer = ''
    start_index = 0
    find_ct = len(number) - k
    while find_ct != 0:
        print('현재 {}개의 수를 더 찾아야 합니다.'.format(find_ct))
        remain_ct = find_ct - 1
        print('리스트의 {}인덱스부터 {}인덱스까지 살펴봅니다.'.format(start_index, len(number) - remain_ct - 1))
        find_str = number[start_index: len(number) - remain_ct]
        print('{}중 가장 큰 수를 찾습니다.'.format(find_str))
        answer += str(max(find_str))
        print('제일 큰 수는 {}이고 해당 숫자의 인덱스는 {}입니다.'.format(max(find_str), find_str.index(max(find_str))))
        start_index = find_str.index(max(find_str)) + 1
        find_ct -= 1
    return answer


def solution2(number, k):
    answer = ''
    start_index = 0
    find_ct = len(number) - k
    while find_ct != 0:
        print('현재 {}개의 숫자를 더 찾아야 합니다.'.format(find_ct))
        if len(number[start_index:]) == find_ct:
            print('찾아야 하는 숫자와 남아있는 문자열의 길이가 같으므로 {}을 그대로 추가합니다.'.format(number[start_index:]))
            answer += str(number[start_index:])
            break
        finish_index = len(number) - find_ct
        # find_str = number[start_index : finish_index + 1]
        max_num = max(number[start_index: finish_index + 1])
        print('문자열 {}에서 가장 큰 수는 {}입니다.'.format(number[start_index: finish_index + 1], max_num))
        answer += str(max_num)
        # 우리가 구한 가장 큰 수의 인덱스는 find_str 문자열의 인덱스이므로 그 전에 있던 문자의 개수인 start_index 를 더하여 새롭게 만든다.
        start_index = number[start_index: finish_index + 1].index(max_num) + 1 + start_index
        find_ct -= 1
    return answer


def solution3(number, k):
    answer = ''
    find_ct = len(number) - k
    while find_ct != 0:
        global i
        if number[0] <= number[1]:
            for i in range(2, len(number)):
                if number[i-1] > number[i]:
                    i = 0
                    break
            if i + 1 == len(number):
                print('남아있는 문자열에서 뒤에서 차례로 뽑으면 됩니다.')
                answer += str(number[-find_ct:])
                break
        elif number[0] >= number[1]:
            for i in range(2, len(number)):
                if number[i-1] < number[i]:
                    i = 0
                    break
            if i + 1 == len(number):
                print('남아있는 문자열에서 차례로 뽑으면 됩니다.')
                answer += str(number[:find_ct])
                break
        if len(number) == find_ct:
            answer += str(number)
            break
        else:
            finish_index = len(number) - find_ct
            max_num = max(number[:finish_index + 1])
            answer += str(max_num)
            number = number[number.index(max_num) + 1:]
        find_ct -= 1
    return answer


print(solution3('1924', 2))
print('=====================================')
print(solution3('1231234', 3))
print('=====================================')
print(solution3('4177252841', 4))
print('=====================================')
print(solution3('417725847', 4))
print('=====================================')
print(solution3('78211111', 2))
