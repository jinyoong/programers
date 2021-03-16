def solution(strings, n):
    answer = []
    st = []
    for word in strings:
        st.append(word[n])
    st = list(set(st))
    st.sort()
    # print(st)
    strings.sort(reverse=False)
    for wd in st:
        for i in range(len(strings)):
            if (wd == strings[i][n]):
                answer.append(strings[i])
    return answer


print(solution(["cart", "bed", "car"],1))