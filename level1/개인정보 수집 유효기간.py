def solution(today, terms, privacies):
    answer = []
    terms_dict = {}

    for term in terms:
        element, time = term.split(" ")
        terms_dict[element] = int(time)

    privacy_list = []

    for privacy_element in privacies:
        privacy, term = privacy_element.split(" ")
        privacy_list.append(after_term(terms_dict[term], privacy))

    today_int = int(today.replace(".", ""))

    for index, privacy_element in enumerate(privacy_list, 1):

        if today_int > privacy_element:
            answer.append(index)

    return answer


def after_term(term, privacy):
    year, month, day = map(int, privacy.split("."))

    month += term
    day -= 1

    if day == 0:
        month -= 1
        day += 28

    while month > 12:
        year += 1
        month -= 12

    result = year * 10000 + month * 100 + day

    return result


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
