def solution(arr):
    #print(arr, len(arr))
    #배열의 길이가 1이 되면 그 원소를 반환
    '''if len(arr) == 1:
        return arr[0]'''
    #배열의 처음 두 수를 이용해 최소공배수를 구하여 배열에 추가
    if len(arr) != 1:
        #만약 처음 두 수 중 앞의 수가 더 크다면 서로 값을 바꿈
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        #큰 수를 작은 수로 나누었을 때 나머지가 0이면 두 수의 최소공배수는 큰 수 자신
        if arr[1] % arr[0] == 0:
            #작은 수는 이제 필요 없으니까 배열에서 삭제
            arr.pop(0)
        #큰 수를 작은 수로 나누었을 때 나머지가 0이 아니면 최소공배수를 구해줘야 함
        else:
            #최대공약수를 구하기 위해 유클리드 호제법 이용
            big = arr[1]
            small = arr[0]
            # 아래는 유클리드 호재법을 이용해서 최대공약수를 구하는 방법
            while big % small != 0:
                big, small = small, big % small
            #구해진 최대공약수를 이용해 두 수의 최소공배수를 구함
            lcm = int(arr[0] * arr[1] / small)
            #처음 두 수를 이용해 최소공배수를 구했으므로 필요 없어진 두 수는 삭제
            del arr[0:2]
            #배열의 맨 앞에 구해진 최소공배수를 추가
            arr.insert(0, lcm)
        #배열의 길이가 1이 될 때까지 해당 함수를 반복
        return solution(arr)
    else:
        return arr[0]








'''def solution(arr):
    answer = 0
    arr.sort(reverse=False)
    # 최소공배수를 쉽게 구하기 위해 오름차순으로 배열 정렬
    while len(arr) >= 2:
        # 배열의 두 수를 이용해 최소공배수를 구하고, 최소공배수를 배열에 추가
        for i in range(2):
            if arr[1] % arr[0] == 0:
                # 두 수 중 작은 수로 나누어 떨어진다는 것은 큰 수 자체가 최소공배수가 된다는 뜻
                arr.pop(0)
                # 따라서 0번째 원소를 제거해준다.
            else:
                big = arr[1]
                small = arr[0]
                # 아래는 유클리드 호재법을 이용해서 최대공약수를 구하는 방법
                while big % small != 0:
                    big, small = small, big % small
                lcm = int(arr[0] * arr[1] / small)
                del arr[0:2]
                arr.insert(0, lcm)
                # 최소공배수가 두 수를 이용해서 새롭게 나왔기 때문에 이용한 두 수를 삭제하고 최소공배수를 맨 앞에 배치
        print(arr)
    answer = arr[0]
    return answer'''


print(solution([2,4,6,8]))
