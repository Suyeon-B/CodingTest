"""
1. 회의 시작 시간(s)으로 정렬 후
2. 회의 끝 시간(e)으로 정렬

정렬된 리스트를 기준으로 e <= s일 때 추가해줌
"""

def meetingRoom(N, meetingTimes):
    meetingTimes = sorted(meetingTimes, key=lambda x:x[0])
    meetingTimes = sorted(meetingTimes, key=lambda x:x[1])

    answer = 1
    last = meetingTimes[0][1]
    for i in range(N-1):
        if last <= meetingTimes[i+1][0]:
            last = meetingTimes[i+1][1]
            answer+=1

    return answer

N = int(input())
meetingTimes = []
for i in range(N):
    mts = []
    for j in range(1):
        s, e = map(int, input().split())
        meetingTimes.append([s, e])

print(meetingRoom(N, meetingTimes))