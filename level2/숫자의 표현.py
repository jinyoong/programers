def solution(n):
    #자기 자신은 어떤 자연수라도 포함되므로 총 개수는 무조건 1 이상
    answer = 1
    #(n-1)/2+1과 (n-1)/2의 합이 연속된 2개의 자연수로 나타낼 수 있는 방법이기 때문에 시점을 저렇게 설정
    #가장 많은 수를 더하는 경우는 1부터 시작하는 경우이므로 종점은 1부터 k까지 더했을 때 n이 되는 수로 잡는 것이 좋다.
    #따라서 k 자리에 들어갈 수 있는 수는 2n의 루트꼴이므로 종점을 아래처럼 설정
    for i in range(int((n-1)/2)+1,int((2*n)**0.5)-1,-1):
        #print('{}부터 연속된 자연수를 더합니다.'.format(i))
        for j in range(i-1,0,-1):
            #print('{}에 {}를 더합니다.'.format(i,j))
            i += j
            if i > n:
                break
            elif i == n:
                answer += 1
                break
    return answer


print(solution(15))


'''answer = 0
def solution(n):
    global answer
    k = n
    if n-k == 0:
        answer += 1
    else:
        n = n-k

for i in range(10,0,-1):
    print(i)'''