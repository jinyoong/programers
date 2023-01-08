def solution(m, musicinfos):
    answer, time = '(None)', 0
    m = make_list(m)

    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(",")
        total_time = calc_time(end) - calc_time(start)

        if len(m) > total_time:
            continue

        melody = make_list(melody)
        is_correct = False

        for i in range(total_time):
            idx = i % len(melody)

            if melody[idx] != m[0]:
                continue

            for j in range(len(m)):

                if melody[(idx + j) % len(melody)] != m[j]:
                    break
            else:
                is_correct = True

            if is_correct:
                break

        if is_correct:

            if total_time > time:
                answer = title
                time = total_time

    return answer


def calc_time(string_time):
    hour, minute = map(int, string_time.split(":"))
    return hour * 60 + minute


def make_list(target_melody):
    result = []

    for i in range(len(target_melody)):
        if target_melody[i] == "#":
            continue

        if i + 1 < len(target_melody) and target_melody[i + 1] == "#":
            temp = target_melody[i:i+2]
        else:
            temp = target_melody[i]

        result.append(temp)

    return result


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("AB", ["12:00,12:03,HELL,AB"]))
