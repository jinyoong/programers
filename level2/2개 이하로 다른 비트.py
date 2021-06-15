def solution(numbers):
    answer = []
    for num in numbers:
        print('\n{}을(를) 합니다.'.format(num))
        num_bit = ''
        while num > 1:
            a, b = divmod(num, 2)
            num_bit = str(b) + num_bit
            num = a
        num_bit = str(num) + num_bit
        print('2진수로 표현하면 {}입니다.'.format(num_bit))
        if num_bit.count('0') >= 1:
            # 2진수 표현에서 0이 있는지 없는지에 따라 달라진다.
            if num_bit[-1] == '0':
                # 만약 2진수 표현에서 맨 뒤에 0이 위치한다면, 이 0을 1로만 바꿔주면 1차이 나는 숫자이므로 조건을 만족한다.
                num_bit = num_bit[::-1].replace('0', '1', 1)
                num_bit = num_bit[::-1]
            else:
                # 0이 맨 뒤에 위치한게 아닌 경우에는 뒤에서부터 처음으로 나온 0과 1의 위치를 바꿔주면 된다.
                num_bit = num_bit[::-1].replace('10', '01', 1)
                num_bit = num_bit[::-1]
                # 조금 복잡하지만 문자열을 리스트로 바꾸지 않고 뒤에서부터 문자를 바꿔준 것
        else:
            # 모두 1로만 이루어진 경우에는 맨 앞에 1을 추가하고 그 다음에는 0이 오면 된다.
            num_bit = '1' + num_bit.replace('1', '0' ,1)
        print('조건을 만족하면서 더 큰 2진수는 {}입니다.'.format(num_bit))

        temp = 0
        for i in range(len(num_bit)):
            temp += (2 ** (len(num_bit)-1-i)) * int(num_bit[i])
        answer.append(temp)
    return answer

print(solution([11, 12, 13, 27, 28, 29, 30]))