def solution(arr):
    answer = []
    #print(len(arr))
    srt = 0
    cnt_all = 0
    while(cnt_all != len(arr)):
        answer.append(arr[srt])
        #print(srt)
        if(srt+1 < len(arr) and arr[srt] == arr[srt+1]):
            fsh = srt
            count = 0
            while(fsh < len(arr) and arr[srt] == arr[fsh]):
                count += 1
                fsh += 1
                #print("마지막 개수는 " + str(fsh))
            cnt_all += count
            #print("총 개수는 " + str(cnt_all))
            srt = cnt_all
        else:
            srt += 1
            cnt_all += 1
            #print("총 개수는 " + str(cnt_all))
    return answer


print(solution([5, 5, 7, 7, 7, 8, 9, 2, 1, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 8]))