from heapq import *
# 최소 힙 구현
def min_heap(scovile):
    heap = [0, scovile[0]]
    for i in range(1, len(scovile)):
        heap.append(scovile[i])
        if heap[i+1] <= heap[i+1 // 2]:
            idx = i+1
            while heap[idx] <= heap[idx // 2]:
                if idx == 1:
                    break
                heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
                idx //= 2

    return heap[1:]


answer = 0


def solution3(scovile, K):
    global answer
    scovile = min_heap(scovile)
    if len(scovile) == 1 and scovile[0] < K:
        return -1
    if scovile[0] >= K:
        return answer
    num1 = scovile.pop(0)
    scovile = min_heap(scovile)
    num2 = scovile.pop(0)
    new_scov = num1 + num2 * 2
    scovile.append(new_scov)
    scovile = min_heap(scovile)
    answer += 1
    return solution3(scovile, K)


def solution(scoville, K):
    answer = 0
    temp = []
    # 섞은 음식의 스코빌 지수를 이용하기 위해 빈 리스트 생성
    scoville.sort()
    # 음식의 스코빌 지수가 제일 작은 값, 두 번째로 작은 값이 필요하므로 오름차순으로 정렬
    # print(scoville)

    for i in range(len(scoville)):
        print('현재 {}번째 인덱스 값인 {}을 확인합니다.'.format(i, scoville[i]))
        if scoville[i] >= K:
            if not temp:
                break
            else:
                if temp[0] >= K:
                    break
                else:
                    scoville = temp
                    if solution(scoville, K) != -1:
                        return answer + solution(scoville, K)
                    else:
                        return -1
        elif scoville[i] == 0 and i != len(scoville) - 1:
            pass
            # 섞어서 사용한 음식의 스코빌 지수는 0으로 초기화 한다.
            # 리스트의 길이를 유지시켜 시간을 줄이기 위해서 삭제하지 않은 것
        else:
            if i == len(scoville) - 1:
                if not temp:
                    return -1
                    # 만약 배열의 마지막 원소 값까지 도달했으면서 temp 가 빈 배열인 경우 섞을 수가 없으므로 -1을 반환
                elif scoville[i] != 0:
                    if scoville[i] <= temp[0]:
                        if scoville[i] + temp[0] * 2 >= K:
                            answer += 1
                            temp.append(temp[0] + scoville[i] * 2)
                            temp.pop(0)
                            scoville[i] = 0
                            print(temp)
                            print(scoville)
                            scoville = temp
                            if solution(scoville, K) != -1:
                                return answer + solution(scoville, K)
                            else:
                                return -1
                        else:
                            return -1
                    else:
                        if temp[0] + scoville[i] * 2 >= K:
                            answer += 1
                            temp.append(temp[0] + scoville[i] * 2)
                            temp.pop(0)
                            scoville[i] = 0
                            print(temp)
                            print(scoville)
                            scoville = temp
                            if solution(scoville, K) != -1:
                                return answer + solution(scoville, K)
                            else:
                                return -1
                        else:
                            return -1
                elif scoville[i] == 0:
                    temp2 = temp
                    return answer + solution(temp2, K)
            else:
                if not temp:
                    # temp 배열이 비어있는 경우 앞 2개의 숫자를 가지고 새로운 스코빌 지수를 생성한다.
                    temp.append(scoville[i] + scoville[i + 1] * 2)
                    scoville[i] = 0
                    scoville[i + 1] = 0
                    answer += 1
                else:
                    # temp 배열이 비어있지 않은 경우, temp 배열의 원소를 이용할지 말지 판단해야 한다.
                    if temp[0] <= scoville[i]:
                        # 만약 temp 배열의 원소가 scoville[i] 원소보다 작거나 같을 경우
                        # 제일 작은 숫자를 temp 배열의 원소로 한다.
                        first_num = temp[0]
                        temp.pop(0)
                        # 그리고 두 번째로 작은 숫자는 scoville[i]로 지정한다.
                        second_num = scoville[i]
                        scoville[i] = 0
                    else:
                        first_num = scoville[i]
                        scoville[i] = 0
                        if temp[0] <= scoville[i + 1]:
                            second_num = temp[0]
                            temp.pop(0)
                        else:
                            second_num = scoville[i + 1]
                            scoville[i + 1] = 0
                    temp.append(first_num + second_num * 2)
                    answer += 1
                print('temp = {}'.format(temp))
                print(scoville)
    print(scoville)
    print(temp)
    return answer


def solution2(scoville, K):
    answer = 0
    temp = []
    # 섞은 음식의 스코빌 지수를 이용하기 위해 빈 리스트 생성
    scoville.sort()
    # 음식의 스코빌 지수가 제일 작은 값, 두 번째로 작은 값이 필요하므로 오름차순으로 정렬

    for i in range(len(scoville)):
        print('현재 {}번째 인덱스 값인 {}을 확인합니다.'.format(i, scoville[i]))
        if scoville[i] >= K:
            break
        elif scoville[i] == 0:
            pass
            # 섞어서 사용한 음식의 스코빌 지수는 0으로 초기화 한다.
            # 리스트의 길이를 유지시켜 시간을 줄이기 위해서 삭제하지 않은 것
        else:
            # 이 경우 i번째 원소가 0도 아니고 K보다 작은 스코빌 지수 값인 것
            if not temp:
                # temp 배열이 비어있는 경우
                # 남은 원소가 1개라면 -1을 반환한다.
                if i == len(scoville) - 1:
                    return -1
                else:
                    # scoville 배열의 앞 2개의 원소를 가지고 연산하면 된다.
                    temp.append(scoville[i] + scoville[i + 1] * 2)
                    scoville[i] = 0
                    scoville[i + 1] = 0
                    # 이용한 음식의 스코빌 지수는 0으로 초기화 한다.
            else:
                # temp 배열이 비어있지 않은 경우
                # 이 경우가 고려할 부분이 많은 분기점이다.
                if i == len(scoville) - 1:
                    # 남은 원소가 1개인 경우 temp에 추가하여 앞 2개의 숫자를 이용한다.
                    temp.append(scoville[i])
                    temp.sort()
                    if temp[0] + temp[1] * 2 >= K:
                        answer += 1
                        return answer


def solution4(scoville, K):
    answer = 0
    heap = []

    for element in scoville:
        heappush(heap, element)

    while True:
        if heap[0] >= K:
            break

        if len(heap) == 1:
            return -1

        minimum = heappop(heap)
        second = heappop(heap)
        heappush(heap, minimum + second * 2)
        answer += 1

    return answer


print('\n' + '-' * 50 + '\n')
print(solution4([2, 1, 3, 9, 10, 12], 7))
# print('\n' + '-' * 50 + '\n')
# print(solution3([1, 2, 9], 7))
# print('\n' + '-' * 50 + '\n')
# print(solution3([1, 1, 1, 1, 1, 1, 30], 20))
# print('\n' + '-' * 50 + '\n')
# print(solution3([1, 1, 1], 8))
# print('\n' + '-' * 50 + '\n')
# print(solution3([3, 5, 7, 23, 1, 2, 8], 35))
# print('\n' + '-' * 50 + '\n')
# print(solution3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 2, 2, 2, 8], 70))
