def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: (len(x), int(x)), reverse=False)
    print(phone_book)
    for i in range(len(phone_book)):
        print('\n{}가 접두어로 포함된 번호가 있는지 확인합니다.'.format(phone_book[i]))
        for j in range(i+1, len(phone_book)):
            print(phone_book[j])
            if len(phone_book[i]) == len(phone_book[j]):
                pass
            else:
                if len(phone_book[i]) < len(phone_book[j]):
                    print('{}에 {}가 접두어로 있는지 확인합니다.'.format(phone_book[j], phone_book[i]))
                    if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                        print('{}에 {}가 있습니다.'.format(phone_book[j], phone_book[i]))
                        return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88",'11']))

def solution2(phone_book):
    len_pb = list(set([len(element) for element in phone_book]))
    len_pb.sort(reverse=False)
    # phone_book 리스트의 원소들의 길이들을 중복을 제거하여 오름차순으로 나열한다.
    print(len_pb)
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

print()
print(solution2(["119", "97674223", "1195524421"]))
print(solution2(["123","456","789"]))
print(solution2(["10","123","1235","567","88",'11']))

# 다른사람 풀이

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True