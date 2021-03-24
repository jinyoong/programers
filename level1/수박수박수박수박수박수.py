def solution(n):
    answer = ''
    subak_list = []
    subak = ["수", "박"]
    if(n%2 == 0):
        subak_list = subak*int(n/2)
    else:
        subak_list = subak*int((n-1)/2)
        subak_list.append(subak[0])
    for word in subak_list:
        answer += word
    return answer

print(solution(10))