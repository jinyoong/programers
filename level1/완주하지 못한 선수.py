def solution(participant, completion):
    participant.sort(reverse=True)
    completion.append(" ")
    completion.sort(reverse=True)
    answer = ''
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            answer = participant[i]
            break
    return answer

# 아래는 준태코드

'''def solution(participant, completion):

    participant_count = []
    participant_member = []
    answer = []

    for i in participant:
        if i in participant_member:
            pass
        else:
            participant_count.append(participant.count(i))
            participant_member.append(i)
    while(sum(participant_count) != 1):
        for i in range(len(participant_member)):
            if participant_member[i] in completion and participant_count[i] > 0:
                participant_count[i] -= 1

    for i in range(len(participant_count)):
        if participant_count[i] != 0:
            answer.append(participant_member[i])

    return "".join(answer)'''


print(solution(["marina", "josipa",'vinko', 'vinko', "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", 'vinko', 'vinko', "nikola"]))