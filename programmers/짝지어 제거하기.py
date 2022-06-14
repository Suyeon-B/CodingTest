from collections import deque, defaultdict


def solution(s):
    s = deque(s)
    answer = [s.popleft()]
    cnt = defaultdict(int)
    if len(s) < 2 or len(set(s)) > len(s)//2:
        return 0
    for _ in range(len(s)):
        now = s.popleft()
        if cnt[now] <= 2 and answer and answer[-1] == now:
            answer.pop()
            del cnt[now]
        else:
            answer.append(now)
            cnt[now] += 1

    if len(answer) == 0:
        return 1
    else:
        return 0

s = "baabaa"
print(solution(s))