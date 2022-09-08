def solution(fees, records):
    """
    입차 후 출차 내역이 없으면 23:59 에 출차한 것으로 본다
    총 주차 시간이 기본 시간 이하일 때는 기본 요금을 청구
    총 주차 시간이 기본 시간 초과일 때는 초과한 시간에 대해 단위 요금 청구
    초과한 시간은 단위 시간으로 나눈 뒤 올림한다
    차량 번호가 작은 자동차부터 주차 요금 정보를 반환
    """
    answer = []
    default_time, default_cost, unit_time, unit_cost = fees

    cars = {}
    for record in records:
        temp = record.split()
        time, car, in_out = temp
        time_temp = list(map(int, time.split(":")))
        time = time_temp[0] * 60 + time_temp[1]
        cars[car] = cars.get(car, []) + [time]

    cars_list = sorted(list(cars.keys()))
    costs = {}

    for car, times in cars.items():
        total = 0

        if len(times) % 2:
            times.append(23 * 60 + 59)

        for i in range(1, len(times), 2):
            out_time = times[i]
            in_time = times[i - 1]
            total += out_time - in_time

        time = total - default_time

        if time <= 0:
            costs[car] = default_cost
            continue

        if time % unit_time:
            costs[car] = (time // unit_time + 1) * unit_cost + default_cost
        else:
            costs[car] = (time // unit_time) * unit_cost + default_cost

    for car_ele in cars_list:
        answer.append(costs[car_ele])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
