# zip을 사용해서 progresses, speeds를 묶었음
# 작업 시 필요한 일수가 기준일보다 작으면 cnt+1해주고,
# 필요한 일수가 커지는 순간 기준 일을 큐에 추가해줌
import math


def solution(prog, spd):
    Q = []
    for p, s in zip(prog, spd):
        if not Q or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]


prog = [93, 30, 55]
spd = [1, 30, 5]
print(solution(prog, spd))
