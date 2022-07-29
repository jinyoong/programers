def solution2(name):

    answer = 0

    stick_index = 0
    total_moving = 0
    alpha_ct = 0
    temp = ['A'] * len(name)

    for i in range(len(name)):
        if temp[i] == 'A' and temp[i] != name[i]:
            if name[i] <= 'N':
                alpha_ct += (ord(name[i]) - ord('A'))
            else:
                alpha_ct += (ord('Z') - ord(name[i])) + 1
    print('이동을 고려하지 않고 알파벳만 변화시킬 때 필요한 이동 수는 {}입니다.'.format(alpha_ct))

    temp[0] = name[0]

    ct = 0

    while temp != list(name):
        ct += 1
        right_move = 0
        left_move = 0
        while True:
            right_move += 1
            if name[(stick_index + right_move) % len(name)] != 'A' \
                    and temp[(stick_index + right_move) % len(name)] != name[(stick_index + right_move) % len(name)]:
                print('{}에서 오른쪽으로 {}번 이동하여 A가 아닌 문자가 나왔습니다.'.format(stick_index, right_move))
                break
        while True:
            left_move += 1
            if name[(stick_index - left_move) % len(name)] != 'A'\
                    and temp[(stick_index - left_move) % len(name)] != name[(stick_index - left_move) % len(name)]:
                print('{}에서 완쪽으로 {}번 이동하여 A가 아닌 문자가 나왔습니다.'.format(stick_index, left_move))
                break
        if right_move <= left_move:
            total_moving += right_move
            stick_index = (stick_index + right_move) % len(name)
            temp[stick_index] = name[stick_index]
        else:
            total_moving += left_move
            stick_index = (stick_index - left_move) % len(name)
            temp[stick_index] = name[stick_index]
        print(temp)
    return alpha_ct + total_moving

# 밑은 지수 풀이

def solution(name):
    # 모든 알파벳이 A가 아니라면 각각 A와의 ord 차이를 구해서 더하면 됨(1~13)
    # A~Z가 25번 (26-1번), 그니까 13 N은 >> 방향 O부터는 << 방향
    # 처음에는 좌우 방향을 처음 한번만 정하고 쭉 유지하는 줄 알았는데 아니었다
    # BBAAAAAC 같은 경우 0번 (오른쪽 1번 이동 > ) 1번 (왼쪽 2번 이동 << ) -1번
    # 이런식으로 이동방향을 바꾼다. 현 위치에서 좌우 중에서 0이 아닌 값이 있는 가까운 곳으로 이동
    rename = [(26 - (ord(n) - ord('A'))) if (ord(n) - ord('A')) > 13 else (ord(n) - ord('A')) for n in name]


    result = 0
    # 0번 인덱스부터 변경 시작
    idx = 0

    # 모두 변경 완료되기 전까지 반복
    while rename != [0] * len(name):
        # 조이스틱 상or하 누른만큼('A'와의 거리만큼) 결과에 더한다
        result += rename[idx]
        # 변경완료했으니 0으로 만들어준다
        rename[idx] = 0

        # 다 바뀌었다면 종료
        if rename == [0] * len(name):
            return result

        # 현재 위치에서 좌우로 0이 아닌 값(바꿔야할 값)이 나올때까지 가본다
        r, l = (1, 1)
        while rename[idx + r] == 0:
            r += 1

        while rename[idx - l] == 0:
            l += 1

        # 왼쪽이 더 가깝다면, 왼쪽으로 간다
        if l < r:
            # 이동한만큼 조이스틱을 <로 움직인거니까 그만큼 결과에 더한다
            result += l
            idx -= l
        # 반대
        else:
            result += r
            idx += r

    return result


def solution3(name):
    # B ~ M 는 위 방향키를 이용, N ~ Z 는 아래 방향키를 이용하는 것이 이득
    answer = 0
    result = [0] * len(name)

    # 좌우 이동을 제외하고 A 로만 이루어진 문자열을 name 문자열로 만드는데 필요한 이동 수를 구해야 한다
    # 좌우 이동을 신경 쓰는데, 이미 A 인 부분은 나중에 이동해도 되니까 표시 해놓자
    for i, alpha in enumerate(name):
        if ord(alpha) >= 78:
            answer += 91 - ord(alpha)
        else:
            answer += ord(alpha) - ord("A")

        if alpha == "A":
            result[i] = 1

    idx = 0
    result[idx] = 1

    # 1. 현재 위치에서 더 0 이 가까운 곳으로 이동해서 1로 바꾸자 => 틀림
    # while 0 in result:
    #
    #     for i in range(len(name)):
    #         right = (idx + i) % len(name)
    #         left = (idx - i) % len(name)
    #
    #         if not result[right]:
    #             idx = right
    #             answer += i
    #             break
    #
    #         if not result[left]:
    #             idx = left
    #             answer += i
    #             break
    #
    #     result[idx] = 1

    # 2. 재귀함수를 이용해서 모든 경우를 살펴보자
    move_count = 987654321

    def all_cases(lst, current, count, length):
        nonlocal move_count

        if move_count <= count:
            return

        if lst == [1] * length and move_count > count:
            move_count = count
            return

        for j in range(length):
            r = (current + j) % length
            l = (current - j) % length

            if not lst[r]:
                lst[r] = 1
                all_cases(lst, r, count + j, length)
                lst[r] = 0

            if not lst[l]:
                lst[l] = 1
                all_cases(lst, l, count + j, length)
                lst[l] = 0

    all_cases(result, idx, 0, len(name))
    answer += move_count
    # print("이동 최솟값 : {}, 정답 : {}".format(move_count, answer + move_count))

    # 3. 연속해서 붙어있는 경우가 문제가 되니까 연속한 경우는 맨 마지막을 기준으로 비교해보자 => 틀림
    # while 0 in result:
    #
    #     print(result)
    #
    #     for i in range(len(name)):
    #         right = (idx + i) % len(name)
    #         left = (idx - i) % len(name)
    #
    #         if not result[right] and result[(right + 1) % len(name)]:
    #             for j in range(i + 1):
    #                 result[(idx + j) % len(name)] = 1
    #             idx = right
    #             answer += i
    #             break
    #
    #         if not result[left] and result[(left - 1) % len(name)]:
    #             for j in range(i + 1):
    #                 result[(idx - j) % len(name)] = 1
    #             idx = left
    #             answer += i
    #             break

    return answer


print(solution3("JAZ"))
print(solution3("JEROEN"))
print(solution3("AAB"))
print(solution3("AABAAAAAAABBB"))
print(solution3("ABABBBBAAABBA"))


'''
print(solution2('JAZ'))
print(solution2('JEROEN'))
print(solution2('JAN'))
print(solution2('AMBULANCE'))
print(solution2('ABAAN'))
print(solution2('ABBANA'))
print(solution2('AABBANA'))
print(solution2('ABBANAA'))
print(solution2('AABBANAA'))
print(solution2('AAAAAAAAA'))
print(solution2('ELEVATER'))
print(solution2('UMBRELLA'))
print(solution2('BBBBABBBB'))
print(solution2('BAABB'))
print(solution2('BAABBBAAA'))
print(solution2('AABBBAB'))
'''

# print(solution("BBBAAAB")) #8
# print(solution("ABABAAAAABA")) #10
# print(solution("CANAAAAANAN")) #48
# print(solution("ABAAAAABAB")) #8
# print(solution("ABABAAAAAB")) #8
# print(solution("BABAAAAB")) #7
# print(solution("AAA")) #0
# print(solution("ABAAAAAAABA")) #6
# print(solution("AAB")) #2
# print(solution("AABAAAAAAABBB")) #11
# print(solution("ZZZ")) #5
# print(solution("BBBBAAAAAB")) #10
# print(solution("BBBBAAAABA")) #12