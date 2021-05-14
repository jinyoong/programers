def solution(w, h):
    answer = 0
    # 가로와 세로의 최대공약수가 존재할 시 해당 사각형은 조그만 사각형이 최대공약수만큼 반복해서 나온다는 것을 알 수 있다.
    # 따라서 먼저 유클리드 호제법을 이용하여 최대공약수부터 구한다.
    big = w
    small= h
    if small > big:
        big, small = small, big
    while small != 0:
        big, small = small, big % small
    gcd = big
    # 작은 사각형의 가로와 세로는 원래 사각형의 가로와 세로를 최대공약수로 나눈 값이다.
    nemo_w = int(w / gcd)
    nemo_h = int(h / gcd)
    # 만약 기울기가 3/2라면 가로로 2칸 간 뒤 세로로 3칸을 올라가야 함을 의미한다.
    # 이 때 세로로 올라가기 시작하는 부분은 가로로 진행한 뒤이므로 1칸을 빼줘야 한다.
    # 즉, 3/2의 경우 가로 2칸, 세로 3칸, 겹치는 부분 1칸 이므로 총 4칸을 직선이 가로지른다고 볼 수 있는 것
    white_block = nemo_h + nemo_w - 1
    entire_white_block = gcd * white_block
    answer = w * h - entire_white_block
    '''b_ct = 1
    temp = 1
    if(nemo_h % 2 == 1):
        loop = int(nemo_h / 2)+2
    else:
        loop = int(nemo_h / 2)+1
    for i in range(1,loop):
        print('\n{}층과 {}층을 시작합니다.'.format(i, nemo_h - i + 1))
        while((nemo_h / nemo_w)*b_ct < i):
            b_ct += 1
        print('시작 블록은 {}번이고 끝 블록은 {}입니다'.format(temp, b_ct))
        print('{}층의 남아있는 블록의 수는 {}개입니다'.format(i, nemo_w - b_ct))
        print('{}층의 남아있는 블록의 수는 {}개입니다'.format(nemo_h - i + 1, temp-1))
        if(nemo_h % 2 == 1 and i == loop-1):
            answer += (nemo_w - b_ct)
        else:
            answer += (nemo_w - b_ct) + temp - 1
        if(((nemo_h / nemo_w) * b_ct) == float(i)):
            temp = b_ct + 1
        else:
            temp = b_ct'''
    return answer



print(solution(8, 12))