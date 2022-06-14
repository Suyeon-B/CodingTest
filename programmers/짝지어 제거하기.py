from collections import deque, defaultdict


def solution(s):
    s = deque(s)
    answer = [s.popleft()]
    # cnt = defaultdict(int)
    if len(s) < 2 or len(set(s)) > len(s)//2:
        return 0
    for _ in range(len(s)):
        now = s.popleft()
        if answer and answer[-1] == now:
            answer.pop()
        else:
            answer.append(now)

    if len(answer) == 0:
        return 1
    else:
        return 0

s = "abaa"
print(solution(s))