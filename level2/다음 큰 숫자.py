def solution(n):
    num = n
    answer = 0
    #먼저 주어진 수를 2진수로 바꾸어 리스트에 저장
    two_list = []
    while n > 1:
        n , y = divmod(n, 2)
        two_list.insert(0, y)
    two_list.insert(0, n)
    final_list = []
    #print('{}을 2진수로 변환하면 {}입니다.'.format(num, two_list))

    #저장된 리스트에서 1의 위치를 바꿔주기만 하면 1의 개수는 동일하지만 다른 수가 나온다.
    #여기서 1의 개수는 같으면서 그 다음으로 큰 수는 제일 뒤에 있는 1부터 앞으로 한 칸씩 이동시키고 그 뒤의 1은 뒤에서부터 채워주면 된다.
    #예를 들어 5 = 101(2)과 1의 개수가 같으면서 그 다음으로 큰 수는 맨 뒤의 1을 앞으로 한 칸 땡긴 6 = 110(2)가 된다.
    #따라서 뒤에 있는 1부터 보는데, 1앞의 수가 0이면 둘의 자리를 바꾸고 반복문을 끝낸다.
    for i in range(len(two_list)-1,-1,-1):
        if i >= 1 and two_list[i] == 1 and two_list[i-1] == 0:
            two_list[i] = 0
            two_list[i-1] = 1
            two_list_1 = two_list[:i+1]
            two_list_2 = []
            #서로 자리를 바꾼 1과 0 뒤의 리스트들은 뒤에서부터 1을 남아있는 개수만큼 채워주면 된다.
            for j in range(i+1, len(two_list)):
                if two_list[j] == 1:
                    two_list_2.append(1)
                else:
                    two_list_2.insert(0, 0)
            final_list = two_list_1 + two_list_2
            #print('{}의 2진수와 1의 개수가 같으면서 다음으로 큰 수는 {}입니다.'.format(num, two_list_1 + two_list_2))
            break
        #만약 해당 리스트의 맨 앞까지 위의 관계가 나오지 않는다면 리스트가 전부 1이거나 맨 앞만 1이라는 의미이므로
        #리스트의 맨 앞에 1을 추가하고 그 다음 수를 0으로 변환한 뒤 위의 과정을 반복.
        elif i == 0:
            two_list[i] = 0
            two_list.insert(0, 1)
            two_list_1 = two_list[:2]
            two_list_2 = []
            for j in range(2, len(two_list)):
                if two_list[j] == 1:
                    two_list_2.append(1)
                else:
                    two_list_2.insert(0, 0)
            final_list = two_list_1 + two_list_2
    #print('{}의 2진수와 1의 개수가 같으면서 다음으로 큰 수는 {}입니다.'.format(num, final_list))

    for k in range(len(final_list)):
        answer += final_list[k]*2**(len(final_list)-1-k)
    return answer


print(solution(6))