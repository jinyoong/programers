def solution(s, n):
    answer = ''
    for word in s:
        if(word == " "):
            answer += word
        elif(65 <= ord(word) <= 90):
            if(ord(word)+n >= 91):
                answer += chr(ord(word)+n-91+65)
            else:
                answer += chr(ord(word)+n)
        else:
            if(ord(word)+n >= 123):
                answer += chr(ord(word)+n-123+97)
            else:
                answer += chr(ord(word)+n)
    return answer

print(solution('zZ',1))