def solution(scores):
    answer = ''
    idx = 0

    for i in range(len(scores)):
        for j in range(i):
            scores[i][j], scores[j][i] = scores[j][i], scores[i][j]

    for score in scores:
        s = [max(score), min(score)]
        if score[idx] in s and score.count(score[idx]) == 1:
            temp = (sum(score) - score[idx]) / (len(score) - 1)
        else:
            temp = sum(score) / len(score)
        print(temp)
        if temp >= 90:
            answer += 'A'
        elif temp >= 80:
            answer += 'B'
        elif temp >= 70:
            answer += 'C'
        elif temp >= 50:
            answer += 'D'
        else:
            answer += 'F'

        idx += 1

    return answer