import math


def solution(prog, spd):
    """
    - 남은 개발 : 100-prog
    - 개발 완료에 필요한 일수 : math.ceil((100-prog)/spd)
                        [7, 3, 9]
    - 결과 : 개발 완료에 필요한 일수가 작아지는 순간까지 cnt+=1하고 배열에 넣고 cnt=0
    """
    more_days = []
    for i in range(len(prog)):
        more_days.append(math.ceil((100-prog[i])/spd[i]))
    result = []
    cnt = 0
    now = more_days[0]
    for i in range(len(more_days)-1):
        cnt += 1
        if now < more_days[i+1]:
            result.append(cnt)
            cnt = 0
            now = more_days[i+1]
    cnt += 1
    result.append(cnt)

    return result


prog = [93, 30, 55]
spd = [1, 30, 5]
print(solution(prog, spd))
