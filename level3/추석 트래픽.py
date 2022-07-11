def solution(lines):
    answer = 0
    times = []

    for line in lines:
        day, time, process = line.split(" ")
        hour, minute, sec = time.split(":")
        print(hour, minute, sec)

    return answer


print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
