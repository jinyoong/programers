def solution(s):
    answer = ''
    small_word = []
    big_word = []
    for word in s:
        if(ord(word) >= 97):
            small_word.append(word)
        else:
            big_word.append(word)
    small_word.sort(reverse=True)
    big_word.sort(reverse=True)
    for i in range(len(small_word)):
        answer += small_word[i]
    for j in range(len(big_word)):
        answer += big_word[j]
    return answer


solution("HappyBirthDay")


'''다른 사람 풀이
s = "HappyBirthDay"
''.join(sorted(s, reverse=True))'''