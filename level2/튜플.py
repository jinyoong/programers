def solution(s):
    answer = []
    tuple_s = s[2:-2].split('},{')
    # 먼저 해당 문자열에서 숫자로 },{ 을 모두 없앤 문자열을 반환한다.
    list_s = []
    for word in tuple_s:
        list_s.append(list(map(int, word.split(','))))
    # tuple_s는 아직 ','가 존재하기 때문에 이를 또 없애주기 위해 리스트의 각 원소에서 콤마(,)를 제거하여 숫자로만 이루어진 리스트를 만든다.
    list_s_sort = sorted(list_s, key=lambda x: len(x), reverse=False)
    # 리스트 원소 리스트의 길이의 오름차순으로 리스트를 정렬한다.
    #print(list_s_sort)
    answer.append(list_s_sort[0][0])
    # answer 리스트에 list_s_sort 리스트의 첫 리스트 원소를 추가한다.
    for i in range(1, len(list_s_sort)):
        answer.append(list(set(list_s_sort[i]) - set(list_s_sort[i - 1]))[0])
        # list_s_sort 리스트의 원소 리스트를 셋 자료형으로 바꾸어 차집합을 구한뒤 다시 차집합을 리스트 자료형으로 변환한 뒤 숫자만 추출하여
        # answer 리스트에 추가한다.
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))

# 다른 사람 풀이

def solution2(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter