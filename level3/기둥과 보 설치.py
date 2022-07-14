def solution(n, build_frame):
    pillar = set()
    beams = set()
    result = set()
    answer = []

    def delete_pillar(r, c):
        # 기둥이 사라지는 경우
        # 기둥의 윗부분과 걸쳐있는 요소들에 영향을 주고, 기둥의 아랫부분과 걸쳐있는 요소에는 영향이 없다
        if (r, c + 1) in pillar:  # 현재 기둥 위에 기둥이 있던 경우 => 보의 한쪽 끝 부분 위에 있어야 한다.
            if (r - 1, c + 1) in beams or (r, c + 1) in beams:
                pass
            else:
                return False

        if (r - 1, c + 1) in beams:  # 현재 기둥 위에 특정 보의 오른쪽 면이 닿아 있던 경우:
            if (r - 1, c) in pillar or ((r - 2, c + 1) in beams and (r, c + 1) in beams):
                pass
            else:
                return False

        if (r, c + 1) in beams:  # 현재 기둥 위에 특정 보의 왼쪽 면이 닿아 있던 경우:
            if (r + 1, c) in pillar or ((r - 1, c + 1) in beams and (r + 1, c + 1) in beams):
                pass
            else:
                return False

        return True

    def delete_beam(r, c):
        # 보가 사라지는 경우
        if (r, c) in pillar:  # 현재 보의 왼쪽 면 위에 기둥이 있던 경우
            if (r - 1, c) in beams or (r, c - 1) in pillar:
                pass
            else:
                return False

        if (r + 1, c) in pillar:  # 현재 보의 오른쪽 면 위에 기둥이 있던 경우
            if (r + 1, c) in beams or (r + 1, c - 1) in pillar:
                pass
            else:
                return False

        if (r + 1, c) in beams:  # 현재 보의 오른쪽 면과 닿은 보가 있던 경우
            if (r + 1, c - 1) in pillar or (r + 2, c - 1) in pillar:
                pass
            else:
                return False

        if (r - 1, c) in beams:  # 현재 보의 왼쪽 면과 닿은 보가 있던 경우
            if (r, c - 1) in pillar or (r - 1, c - 1) in pillar:
                pass
            else:
                return False

        return True

    for build_ele in build_frame:
        x, y, a, b = build_ele

        if a == 0:  # 기둥인 경우
            if b:  # 설치의 경우
                if y == 0 or (x, y - 1) in pillar or (x, y) in beams or (x - 1, y) in beams:
                    result.add((x, y, a))
                    pillar.add((x, y))
            else:  # 삭제의 경우
                if delete_pillar(x, y):
                    result.remove((x, y, a))
                    pillar.remove((x, y))

        else:  # 보인 경우 (x, y) 부터 (x + 1, y) 까지가 보의 영역
            if b:
                if (x, y - 1) in pillar or (x + 1, y - 1) in pillar or ((x - 1, y) in beams and (x + 1, y) in beams):
                    result.add((x, y, a))
                    beams.add((x, y))
            else:
                if delete_beam(x, y):
                    result.remove((x, y, a))
                    beams.remove((x, y))

    for set_ele in result:
        answer.append(list(set_ele))

    answer.sort(key=lambda k: (k[0], k[1], k[2]))

    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))