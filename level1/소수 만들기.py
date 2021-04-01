def solution(nums):
    answer = 0
    p_list = [2]
    # 2는 소수 중 유일한 짝수이므로 그냥 추가해 놓고 시작한다.
    nums.sort(reverse=True)
    # 주어진 배열을 내림차순으로 정렬
    max_num = 0
    print(nums)
    # 주어진 배열에서 3개를 뽑아 만들 수 있는 제일 큰 수 중에서만 소수를 선택하면 된다.
    for num in nums[0:3]:
        max_num += num
        # 첫 3개의 숫자를 뽑아 최댓값을 구한다.
    for i in range(3,max_num+1):
        # 3과 최댓값 사이에 존재하는 소수들을 먼저 소수 배열에 추가한다.
        for j in range(2, int(i**0.5)+3):
            if(i%j == 0):
                break
        else:
            p_list += [i]
    print(p_list)
    # 구한 소수 배열을 먼저 프린트해본다.
    for j in range(0,len(nums)-2):
        # 3개를 뽑아서 더하므로, 제일 큰 수는 아무리 작더라도 배열 뒤에서 3번째까지만 선택 가능하다.
        print('{}(이)가 제일 큰 수'.format(nums[j]))
        for k in range(j+1, len(nums)-1):
            # 두 번째로 큰 수는 첫뻔째 수 바로 뒤부터 뒤에서 2번째 수까지 중에서 선택한다.
            print('{}(이)가 두번째 수'.format(nums[k]))
            for n in range(k+1, len(nums)):
                print('{}(이)가 세번째 수'.format(nums[n]))
                if(nums[j] + nums[k] + nums[n] in p_list):
                    # 3개의 숫자를 더한 값이 소수 배열에 있으면 answer에 1을 추가한다.
                    print(nums[j] + nums[k] + nums[n])
                    answer += 1
    return answer


print(solution([1,2,7,6,4]))