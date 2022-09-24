def solution(cacheSize, cities):
    answer = 0
    city_set = []

    for city_name in cities:
        city = city_name.lower()
        if city not in city_set:

            answer += 5
            city_set.append(city)

            if len(city_set) == cacheSize + 1:
                city_set.pop(0)
            continue

        if city in city_set:
            city_set.remove(city)
            city_set.append(city)
            answer += 1

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
