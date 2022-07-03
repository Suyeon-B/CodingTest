# 시간 초과 개선 필요
from sys import stdin, stdout

stdin = open("input.txt",'r')
input = stdin.readline

# parsing
string = input().strip()
n = int(input().strip())
command, stack = [], ["0"]
for _ in range(n):
    command.append(input().strip().split())
for s in string:
    stack.append(s)
    stack.append('0')

curr = len(stack)-1
for c in command:
    if c[0] == "L": # 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
        if curr > 1:
            curr -= 2
        else:
            curr = 0
    elif c[0] == "D": # 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
        if curr < len(stack) - 2:
            curr += 2
        else:
            curr = len(stack)-1
    elif c[0] == "B": # 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
        if curr > 1:
            stack.pop(curr)
            stack.pop(curr-1)
            curr -= 2
    else: # P $ = $라는 문자를 커서 왼쪽에 추가함
        if curr > 2:
            stack.insert(curr, c[1])
            stack.insert(curr, "0")
        else:
            stack.insert(0, c[1])
            stack.insert(0, "0")
        curr += 2

print("".join("".join(stack).split("0"))) # yxz