def solution(s):
    if s[0] == ")" or s[-1] == "(":
        return False
    else:
        temp_list = [s[0]]
        for i in range(1, len(s)):
            temp_list.append(s[i])
            #print(temp_list)
            if len(temp_list) > 1 :
                if temp_list[-2] == '(' and temp_list[-1] == ")":
                    temp_list.pop()
                    temp_list.pop()
        if len(temp_list) == 0:
            return True
        else:
            return False

print(solution('((0()'))