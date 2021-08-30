def solution(price, money, count):
    need_money = 0
    temp = 0
    for i in range(count):
        temp += price
        need_money += temp
    if money >= need_money:
        return 0
    answer = need_money - money
    return answer
