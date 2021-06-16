def solution(s):
    answer = []

    if s == '1':
        answer = [0, 0]
    else:
        ch_ct = 1
        zero_ct = 0
        t = s.replace('0', '')
        zero_ct = len(s) - len(t)
        # print('변환 : {}, 없어진 0 개수 : {}'.format(t, zero_ct))

        while True:
            if t == '1':
                break
            temp = ''
            num = len(t)
            while num > 1:
                a, b = divmod(num, 2)
                temp = str(b) + temp
                num = a
            temp = str(num) + temp
            t = temp.replace('0', '')
            # print('이진 변환 이전 : {}, 이진 변환 결과 : {}'.format(temp, t))
            zero_ct += (len(temp) - len(t))
            # print('없어진 0 개수 : {}'.format(len(temp) - len(t)))
            ch_ct += 1
        answer = [ch_ct, zero_ct]
    return answer

print(solution('110010101001'))
print(solution("01110"))
print(solution('1111111'))
print(solution('1'))