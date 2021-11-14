def num_sort(number):
    result = ""
    n = number[0][0]  # 어떤 수로 시작하는 숫자들인지
    maximum = max(map(len, number))  # 해당 숫자들 중 가장 긴 길이
    temp = [[idx, value, value] for idx, value in enumerate(number)]  # 숫자의 위치, 바꿀 숫자, 원래 숫자를 담을 2중 리스트
    for num in temp:
        num[1] += n * (maximum - len(num[1]))  # 21, 212 같은 경우라면 모두 3자리 숫자로 바꿔주는데 n 으로 추가해준다

    sorted_temp = sorted(temp, key=lambda x: (x[1], x[2][-1]), reverse=True)  # 바꾼 숫자들의 크기로 나열하면서, 원래 끝 숫자가 큰 순서로 정렬

    for i in range(len(number)):
        result += number[sorted_temp[i][0]]

    return result


def solution(numbers):
    num_lst = [[] for _ in range(10)]  # i번째 위치에는 i로 시작하는 숫자들이 들어간다
    for num in numbers:
        temp = str(num)
        num_lst[int(temp[0])].append(temp)

    answer = ''

    for number in num_lst[::-1]:  # 가장 큰 수를 만들려면 큰 수부터 앞에 와야 한다
        if not number:  # 원소가 비어있으면 넘어감
            continue
        if len(number) == 1:  # 원소 리스트에 숫자가 1개뿐이라면 해당 숫자를 그냥 넣는다
            answer += number[0]
            continue
        answer += num_sort(number)  # 원소 리스트에 숫자가 여러개라면 고려해야할 사항이 생긴다

    return str(int(answer))


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
print(solution([40, 403]))  # 40403
print(solution([2, 20, 200]))  # 220200
print(solution([0, 0, 0, 0]))  # 0
print(solution([0, 0, 70]))  # 7000
print(solution([12, 121]))  # 12121
print(solution([21, 212]))  # 21221
print(solution([0, 0, 0, 1000]))  # 1000000
print(solution([34, 343]))
print(solution([33, 30, 3]))
print(solution([997, 9]))
print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([412, 41]))
print(solution([3, 30, 34, 4, 40, 42, 421, 423, 45]))
print(solution([1, 0, 2, 2, 3, 3]))
print(solution([1, 101, 1001, 10101]))

