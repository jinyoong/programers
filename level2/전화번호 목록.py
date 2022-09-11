def solution(phone_book):
    len_pb = list(set([len(element) for element in phone_book]))
    len_pb.sort(reverse=False)
    # phone_book 리스트의 원소들의 길이들을 중복을 제거하여 오름차순으로 나열한다.
    if len(len_pb) == 1:
        return True
        # 만약 len_pb의 길이가 1이라면 phone_book 리스트가 길이가 같은 문자열들로만 이루어졌다는 의미이므로
        # 접두어를 포함하는 번호는 존재할 수 없다.
    else:
        for num in len_pb:
            temp = set([ele[:num] for ele in phone_book if len(ele) > num])
            # phone_book의 원소들 중에서 길이가 num 이상인 원소들을 num 인덱스 이전까지 추출하여 set 자료형으로 변환한다.
            pb = set([ele for ele in phone_book if len(ele) == num])
            # phone_book의 원소들 중 길이가 num인 원소들을 포함한 set 자료형 pb를 만든다.
            if temp & pb:
                # 만약 pb와 temp의 교집합이 공집합이 아니라면 접두어를 포함한 번호가 있다는 의미가 된다.
                return False
    return True
