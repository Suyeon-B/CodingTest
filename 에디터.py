from sys import stdin, stdout

stdin = open("input.txt",'r')
input = stdin.readline

# parsing
string = input().strip()
n = int(input().strip())
command, stack = [], []
for _ in range(n):
    command.append(input().strip().split())
for s in string:
    stack.append(s)
    stack.append('0')

curr = len(stack)-1
for c in command:
    if c[0] == "P":
        stack.insert(curr, c[1])
        stack.insert(curr+1, "0")
        curr = curr + 1
    elif c[0] == "B":
        stack.pop(curr)
        stack.pop(curr)
        curr = curr + 1
    elif c[0] == "L":
        if curr > 1:
            curr -= 2
        if curr == 1:
            curr = 0
    else:
        if curr < len(stack)-3:
            if curr == 0:
                curr += 3
            else:
                curr += 2
print("".join("".join(stack).split("0")))

