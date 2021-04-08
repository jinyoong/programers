def solution(board, moves):
    answer = 0
    result_list = []
    for i in moves:
        print('{}번째 인형을 뽑습니다'.format(i))
        for j in range(len(board)):
            #print('가장 위의 인형을 탐색합니다')
            if(board[j][i-1] != 0):
                print('가장 위의 인형은 {}입니다.'.format(board[j][i-1]))
                result_list.append(board[j][i-1])
                board[j][i-1] = 0
                break
    print(result_list)
    for n in range(len(result_list)):
        for k in range(1,len(result_list)):
            if(result_list[k-1] == result_list[k]):
                answer += 2
                result_list = result_list[:k-1] + result_list[k+1:]
                print(result_list)
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[0,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))