def solution(enroll, referral, seller, amount):
    """
    enroll : 조직 구성원들의 이름
    referral : i 번째 이름은 enroll 의 i 번째 판매원을 조직에 참여시킨 사람의 이름 => enroll i 번째 사람의 추천인 이름
    seller : i 번째 이름은 i 번째 집계 데이터를 판매한 판매원의 이름
    amount : i 번째 숫자는 i 번째 판매량을 의미 (100을 곱해야 정확한 이익금)
    트리로 만들었을 때 자신의 부모 노드는 자식 노드가 가질 값의 10% 를 가져가고, 자식 노드는 원래 값의 90% 만 가져간다.
    이 과정은 루트 노드를 만나거나, 자식 노드가 가질 값의 10% (//연산) 의 결과가 1 미만인 경우가 될 때까지 반복된다.
    """
    answer = {name: 0 for name in enroll}

    # 먼저 부모와 자식 관계를 한 눈에 파악하기 위해 인접리스트를 만들자.
    # 2차원 배열의 원소 배열의 0 번째 이름은 추천인이고, 나머지 원소들은 해당 추천인에 의해 조직에 참여한 사람이다.
    # adj_lst = [['center']]
    #
    # for i in range(len(enroll)):
    #
    #     if referral[i] == '-':
    #         adj_lst[0].append(enroll[i])
    #         continue
    #
    #     for ele in adj_lst:
    #         if referral[i] == ele[0]:
    #             ele.append(enroll[i])
    #             break
    #
    #     else:
    #         adj_lst.append([referral[i], enroll[i]])

    # adj_dict = {'center': set()}
    # for i in range(len(enroll)):
    #
    #     if referral[i] == '-':
    #         adj_dict['center'].add(enroll[i])
    #         continue
    #
    #     if referral[i] in adj_dict.keys():
    #         adj_dict[referral[i]].add(enroll[i])
    #
    #     else:
    #         adj_dict[referral[i]] = {enroll[i]}

    adj_dict = {}
    for i in range(len(enroll)):

        adj_dict[enroll[i]] = referral[i]

    # 판매원의 이름과 해당 판매원의 이익금으로 분배한다.
    # 여기서 판매원의 이름이 여러번 나온다고 한 번에 더해서 돌리면 안된다. => 합치고 나서 이상해질 수 있으니까
    for i in range(len(seller)):
        child = seller[i]
        money = amount[i] * 100
        parent = ''

        # 우선 이익금의 10%(정수만)가 1원 이상인 경우에만 반복해야 한다.
        while money >= 10:

            parent = adj_dict[child]

            # 만약 추천인이 center 인 경우 while 문 종료
            temp = money // 10
            answer[child] += money - temp
            money = temp
            child = parent

            if child == '-':
                break

        if child == '-':
            continue

        answer[child] += money

    return list(answer.values())


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10],))

