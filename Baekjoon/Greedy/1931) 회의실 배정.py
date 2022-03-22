"""
1. 첫 번째 숫자로 정렬
2. 텀으로 정렬

1번 기준으로 순회하며
2번 기준으로 선착순 선택
"""

def meetingRoom(N, meetingTimes):
    sortedByStart = meetingTimes.sort(key=lambda x:x[0])
    sortedByTerm = meetingTimes.sort(key=lambda x:x[-1])

    answer = []
    for i in range(N):
        for j in range(N):
            if sortedByStart[i] == sortedByTerm[j]:
                if answer[-1][-1] < sortedByStart[i]:
                    answer.append(sortedByStart[i])

    return len(answer)

N = int(input())
meetingTimes = []
term = 0
for i in range(N):
    mts = []
    for j in range(1):
        s, e = map(int, input().split())
        term = abs(s - e)
        mts.append([s, e, term])
    meetingTimes.append(mts)

print(meetingRoom(N, meetingTimes))