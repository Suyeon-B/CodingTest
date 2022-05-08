from collections import defaultdict


def solution(line):
    answer = []

    # 키보드 셋팅
    temp = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
    keyboard = defaultdict(tuple)
    for i in range(2):
        for j in range(10):
            keyboard[temp[i][j]] = [i, j]

    # 손의 초기 위치
    left, right = [1, 0], [1, 9]
    # get solution
    for l in line:
        left_hor, left_ver = abs(
            keyboard[l][1] - left[1]), abs(keyboard[l][0] - left[0])
        right_hor, right_ver = abs(
            keyboard[l][1] - right[1]), abs(keyboard[l][0] - right[0])

        left_manhatt = left_hor+left_ver
        right_manhatt = right_hor+right_ver

        if left_manhatt < right_manhatt:
            answer.append(0)
            left = keyboard[l]
        elif left_manhatt > right_manhatt:
            answer.append(1)
            right = keyboard[l]
        else:
            if left_hor < right_hor:
                answer.append(0)
                left = keyboard[l]
            elif left_hor > right_hor:
                answer.append(1)
                right = keyboard[l]
            else:
                if keyboard[l][1] < 5:
                    answer.append(0)
                    left = keyboard[l]
                else:
                    answer.append(1)
                    right = keyboard[l]

    return answer


line = "Q4OYPI"
print(solution(line))
