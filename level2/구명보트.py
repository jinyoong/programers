def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while people:
        print(people)
        if people[0] * 2 <= limit:
            print('남아있는 사람들은 아무렇게 짝지워 태워도 무게를 초과하지 않습니다.')
            if len(people) % 2 == 0 :
                answer += int(len(people) / 2)
            else:
                answer += int(len(people) / 2) + 1
            break
        else:
            if people[0] + people[-1] <= limit and len(people) >= 2:
                print('정원이 {}kg인 구명보트에 몸무게가 {}, {}인 두 사람이 탑니다.'.format(limit, people[0], people[-1]))
                answer += 1
                people.pop(0)
                people.pop(-1)
            else:
                print('정원이 {}kg인 구명보트에 몸무게가 {}인 사람이 한 명 탑니다.'.format(limit, people[0]))
                answer += 1
                people.pop(0)

    return answer
# 위 코드는 효율성에서 탈락. pop() 함수는 리스트를 전체 탐색해서 시간을 많이 잡아 먹는다.
# 아래처럼 원소를 없애지 않고 하는 방법 이용

def solution2(people, limit):
    answer = 0
    people.sort(reverse=True)
    j = 1
    for i in range(len(people)):
        print('{}인덱스를 살펴봅니다.'.format(i))
        if people[i] * 2 <= limit:
            print('남아있는 사람들은 아무렇게 짝지워 태워도 무게를 초과하지 않습니다.')
            if (len(people) - j - i + 1) % 2 == 0:
                answer += int((len(people) - j - i + 1) / 2)
            else:
                answer += int((len(people) - j - i + 1) / 2) + 1
            break
        else:
            if people[i] + people[-j] <= limit and (len(people) - i) >= 2:
                print('정원이 {}kg인 구명보트에 몸무게가 {}, {}인 두 사람이 탑니다.'.format(limit, people[i], people[-j]))
                answer += 1
                j += 1
            else:
                print('정원이 {}kg인 구명보트에 몸무게가 {}인 사람이 한 명 탑니다.'.format(limit, people[i]))
                answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
print('==============================================')
print(solution([70, 80, 50], 100))
print('==============================================')
print(solution2([70, 50, 80, 50], 100))
print(solution2([70, 80, 50], 100))