def solution(n, words):
    answer = []

    word = words[0]

    for i in range(1, len(words)):

        if words[i][0] == words[i - 1][-1]:
            if words[i] in words[:i]:
                # print('이미 한 번 나온 단어입니다.')
                if (i + 1) % n == 0:
                    answer.append(n)
                else:
                    answer.append((i + 1) % n)
                if ((i + 1) / n) % 1 == 0:
                    answer.append((i + 1) // n)
                else:
                    answer.append((i + 1) // n + 1)
                break
        else:
            # print('끝말잇기 규칙에 맞지 않습니다.')
            if (i + 1) % n == 0:
                answer.append(n)
            else:
                answer.append((i + 1) % n)
            if ((i + 1) / n) % 1 == 0:
                answer.append((i + 1) // n)
            else:
                answer.append((i + 1) // n + 1)
            break
    else:
        answer = [0, 0]

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))