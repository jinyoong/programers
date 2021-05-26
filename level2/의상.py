def solution(clothes):
    answer = 0
    part_list = list(set([part[1] for part in clothes]))
    # print(part_list)
    clothes_ct = len(part_list)
    sub_part = []
    for i in range(1<<clothes_ct):
        temp = []
        # 1 비트를 clothes_ct 만큼 왼쪽으로 이동시킨다.
        # 만약 1<<2이면 100 이 되므로 2^2 를 의미하는 숫자가 된다.
        # 부분 집합의 개수라 할 수 있다.
        for j in range(clothes_ct + 1):
            # 원소의 수 만큼 비트를 비교
            if i & (1<<j):
                # i의 j번째 비트가 1이면 j번째 원소 출력
                temp.append(part_list[j])
        # 여기서 공집합의 경우는 볼 필요가 없으므로 제외하여 추가한다.
        if temp:
            sub_part.append(temp)
    print(sub_part)
    for sub in sub_part:
        temp_ct = 1
        # print('\n현재 {}에 있는 부위별로 옷을 최소 1개 이상 입었을 경우를 살펴봅니다.'.format(sub))
        for i in range(len(sub)):
            # print('{}에서 {}부위의 옷이 총 몇 벌 있는지 살펴봅니다.'.format(sub, sub[i]))
            sub_ct = 0
            for cloth in clothes:
                if cloth[1] == sub[i]:
                    sub_ct += 1
            # print('{}벌 있습니다.'.format(sub_ct))
            temp_ct *= sub_ct
        # print('{}에 있는 부위별로 옷을 최소 1개 이상 입었을 경우 만들 수 있는 총 경우의 수는 {}가지 입니다.'.format(sub, temp_ct))
        answer += temp_ct
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

def solution2(clothes):
    answer = 1
    part_list = list(set([part[1] for part in clothes]))
    # 먼저 몇 개의 부위가 있는지부터 리스트에 채워 넣는다.
    for part in part_list:
        # 리스트에 있는 부위별로 총 몇 벌의 있는지 구한다.
        sub_ct = 0
        for cloth in clothes:
            if cloth[1] == part:
                sub_ct += 1
        # 각 부위별 옷의 총 개수를 구하면 해당 수에 1을 더한뒤 answer에 곱한다.
        # 예를 들어 모자 2개, 상의 2개, 하의 2개가 있는 경우를 생각하자
        # 각 부위별로 안 입는다는 선택지도 있으므로 부위별로 총 개수를 1씩 더한다.
        # 그렇게 되면 모자 3개, 상의 3개, 하의 3개 와 같이 되는데
        # 이것을 전부 곱하면 하나도 안 입는 경우부터 각 부위별로 1개씩 입었을 경우인 27가지 경우가 나온다.
        # 우리는 적어도 1벌의 옷을 입어야 하므로 하나도 안 입는 경우 1개를 전체에서 빼주면 되는 것
        answer *= (sub_ct + 1)
    return answer - 1

print(solution2([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))