def solution(files):
    answer = []
    list_files = [['', '', ''] for i in range(len(files))]
    # 우선 files 배열의 각 문자열을 HEAD, NUM, TAIL 부분으로 나눌 빈 2차원 배열을 생성한다.
    # 2차원 배열을 먼저 생성한 이유는 길이를 미리 정해놓아 append() 함수를 쓰지 않고 각 인덱스에 직접 접근하기 위해서이다.
    for head in files:
        # 먼저 files 배열의 각 문자열에서 HEAD 부분부터 추출한다.
        for i in range(len(head)):
            # HEAD는 숫자가 아닌 문자로 이루어져있고 각 문자열을 알파벳부터 시작하므로 가장 먼저 숫자가 나오는 인덱스 직전까지가 HEAD부분이 된다.
            if head[i].isdigit():
                # 따라서 2차원 배열의 원소 배열 0번 인덱스에 HEAD 값을 넣어준다.
                list_files[files.index(head)][0] = head[:i]
                # 반복문을 쭉 할 필요는 없으므로 HEAD 부분을 다 구했으면 바로 break로 빠져나가자
                break

        # 다음으로 NUM과 TAIL 부분을 구한다.
        # NUM만 구하면 그 이후는 전부 TAIL이므로 반복문은 하나만 더 있으면 된다.
        for j in range(i, len(head)):
            # HEAD를 구할 때 사용한 i 변수에는 숫자가 처음 나오게 된 인덱스가 저장되어 있으므로 그것을 활용한다.
            # 숫자로만 이루어진 것을 찾아야 하므로 not isdigit()을 이용하여 처음으로 숫자가 아닌 다른 문자가 나온 인덱스를 찾아낸다.
            if not head[j].isdigit():
                # 위의 조건을 거쳐 나온 j 인덱스 직전까지가 NUM 부분이며, j 인덱스 이후가 TAIL 부분에 저장된다.
                list_files[files.index(head)][1] = head[i:j]
                # 2차원 배열의 원소 배열 1인덱스에 NUM 값을 넣어준다.
                list_files[files.index(head)][2] = head[j:]
                # 2차원 배열의 원소 배열 2인덱스에 TAIL 값을 넣어준다.
                break
                # 역시 break로 반복문에서 걸리는 시간을 최대한 줄여준다.

        # 이 때 TAIL이 공백인 문자열이 존재할 수 있는데, 위의 반복문은 숫자가 아닌 인덱스가 나올 때 조건문을 빠져나오므로 코드가 끝나지 않는 경우가 있다.
        # 그것은 각 문자열이 HEAD, NUM 으로만 이루어진 경우인데, 이 경우는 j 인덱스가 각 문자열의 끝까지 간 경우에 해당한다.
        # 따라서 j + 1이 문자열의 길이와 같으면 TAIL부분은 공백으로 처리하고 NUM 부분은 i 인덱스 이후부터 문자열의 끝까지로 저장한다.
        if j + 1 == len(head):
            list_files[files.index(head)][1] = head[i:]
            list_files[files.index(head)][2] = ''

    # 얻어낸 2차원 배열에서 우리는 HEAD와 NUM으로 다중 조건 정렬을 하면 되므로 아래처럼 처리한다.
    # 우선 알파벳은 대소문자를 구별하지 않은 채로 사전순이므로 upper()함수를 적용한 상태에서 먼저 정렬한다.
    # 그 뒤에는 NUM을 기준으로 정렬해야 하는데 앞에 0을 없애주기 위해 NUM 문자열을 int()함수를 사용하여 정수형 자료로 변경하여 2번째 조건으로 정렬해준다.
    list_files2 = sorted(list_files, key=lambda x: (x[0].upper(), int(x[1])), reverse=False)

    # 2차원 배열의 각 원소 배열 안의 문자열을 모두 합한 뒤 answer 배열에 저장해야 하므로 반복문으로 진행한다.
    for sub_list in list_files2:
        temp = ''
        for i in range(len(sub_list)):
            temp += sub_list[i]
        answer.append(temp)

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print('='*100)
print(solution(["F-15", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))