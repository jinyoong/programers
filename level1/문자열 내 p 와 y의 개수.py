def solution(s):
    answer = True
    s= s.lower()
    p_ct = 0
    y_ct = 0
    for word in s:
        if(word == "p"):
            p_ct += 1
        elif(word == "y"):
            y_ct += 1
    print(p_ct)
    print(y_ct)
    if(p_ct == y_ct):
        return True
    else:
        return False


solution("pPyy")