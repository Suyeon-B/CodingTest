"""
IDEA
- len(set(s)) = len(s)//2 or len(s)//2+1
- 아니라면, 팰린드롬이 아님

- 맞다면 알파벳 수 세어서, set한 알파벳을 sort한 리스트 순으로 양끝에 넣어줌

"""
from sys import stdin
from collections import Counter, deque
stdin = open("input.txt", 'r')
input = stdin.readline

s = input().strip()
alpha = sorted(list(set(s)), reverse=True)
alpha_cnt = Counter(s)
answer = deque([])
mid = ""
# 팰린드롬 가능한 경우
if len(alpha) == len(s)//2 or len(alpha) == len(s)//2+1:
    # 홀수 길이인 경우
    if len(s) % 2 == 1:
        for a in alpha:
            if alpha_cnt[a] > 1:
                while alpha_cnt[a] > 1:
                    answer.appendleft(a)
                    answer.append(a)
                    alpha_cnt[a] -= 2
                    if alpha_cnt[a] == 1:
                        mid = a
            else:
                mid = a
                continue
        answer.insert(len(s)//2, mid)
    else:  # 짝수 길이인 경우
        if len(s) == 2:
            print("I'm Sorry Hansoo")
        for a in alpha:
            while alpha_cnt[a]:
                answer.appendleft(a)
                answer.append(a)
                alpha_cnt[a] -= 2

    # 출력
    print("".join(answer))

# 팰린드롬 불가능한 경우
else:
    print("I'm Sorry Hansoo")
