def solution(n):
    answer = 1
    for i in range(3, n+1):
        #2 이상이므로 2는 항상 소수다.
        #print('지금은 {}를 판단하는 중입니다.'.format(i))
        for j in range(2, round(i**0.5)+1):
            #소수는 1과 자기 자신을 약수로 가진다
            #약수가 있는 경우 짝이 있으므로 전체의 반 정도만 판단해도 된다. 예를 들면 8의 약수 2는 4와 짝이다
            #따라서 1과 자기 자신을 제와한 약수가 존재하지 않으면 소수다.
            if(i%j == 0):
                #만약 약수가 하나라도 있으면 소수가 아니므로
                break
        else:
            answer += 1
    return answer

print(solution(10))