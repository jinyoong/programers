def solution(n, t, m, timetable):
    """
    하루 n 회 t 분 간격으로 오며, 한 버스에 m 명 탈 수 있다
    """
    timetable.sort()
    length = len(timetable)
    idx = 0
    shuttle_time = 540

    for i in range(n-1):
        cnt = 0
        cur_idx = idx

        for j in range(cur_idx, length):
            crew_h, crew_m = map(int, timetable[j].split(":"))
            crew_time = crew_h * 60 + crew_m
            if crew_time <= shuttle_time:
                cnt += 1
                idx += 1

            if cnt == m or crew_time > shuttle_time:
                break

        shuttle_time += t

    if length - idx < m:
        answer = number_to_time(shuttle_time)
        return answer

    crews = {}
    for time in timetable[idx:]:
        crews[time] = crews.get(time, 0) + 1

    total = 0
    result = 0
    for time, cnt in crews.items():
        crew_h, crew_m = map(int, time.split(":"))
        crew_time = crew_h * 60 + crew_m
        if total + cnt >= m:
            result = crew_time - 1
            break
        total += cnt

    if result > shuttle_time:
        result = shuttle_time

    answer = number_to_time(result)
    return answer


def number_to_time(number):
    hour, minute = divmod(number, 60)
    str_hour = "0" + str(hour) if len(str(hour)) <= 1 else str(hour)
    str_minute = "0" + str(minute) if len(str(minute)) <= 1 else str(minute)
    return str_hour + ":" + str_minute


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                            "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(5, 10, 2, ["09:35"] * 12))
print(solution(1, 10, 3, ["08:55", "08:55", "08:59"]))
