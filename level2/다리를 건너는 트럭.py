def solution(bridge_length, weight, truck_weights):
    answer = 1
    on_bridge = []
    # 다리를 건너는 트럭들을 담을 리스트
    truck_road = [0]*len(truck_weights)
    # 각 트럭들이 현재 다리를 지난 길이를 담은 리스트
    total_weight = 0
    # 다리 위에 있는 트럭들의 총 무게 수
    start, finish = 0, 0
    # truck_road 리스트의 원소에 접근하기 위해 인덱스를 변수로 지정


    while on_bridge or truck_weights:
        # 다리를 지나는 트럭, 남아있는 트럭이 하나도 없을 경우 멈춘다.
        answer += 1
        # 1초가 흐름
        # print(answer, on_bridge, truck_weights, truck_road)
        if truck_weights:
            # 남아있는 트럭이 있는 경우
            if total_weight + truck_weights[0] <= weight:
                # 현재 다리 위에 있는 트럭들의 총 무게에 다음 트럭이 올라갈 수 있는지 판단
                finish += 1
                # 트럭이 추가로 1대 올라간다면 finish 변수에 1을 추가한다.
                # truck_road 리스트의 인덱스를 현재 트럭수에 맞추기 위함

                total_weight += truck_weights[0]
                on_bridge.append(truck_weights[0])
                truck_weights.pop(0)

        for i in range(start, finish):
            truck_road[i] += 1
            # 다리를 지나는 트럭들은 1초에 1씩 이동하므로 start부터 finish - 1까지의 인덱스 번호를 가진 트럭들의 거리를 1씩 증가시킨다.

        if truck_road[start] == bridge_length:
            start += 1
            # 만약 트럭 중에 다리 길이 만큼 이동한 트럭이 있으면 on_bridge 리스트에서 제거한다.
            # 그리고 다음 트럭부터 이동 거리를 1씩 증가시켜야 하므로 start 변수에 1을 더한다.
            total_weight -= on_bridge[0]
            on_bridge.pop(0)

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))