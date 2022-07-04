"""
시간 초과 개선 버전
1.bomb 끝 문자열과 같아지는 순간에, bomb 길이만큼 같은지 확인.
2.bomb 문자열의 길이만큼 삭제 & 문자열 끝까지 반복
"""
from sys import stdin

stdin = open("input.txt",'r')
input = stdin.readline

string = input().strip()
bomb = input().strip()

lastChar = bomb[-1]
stack = []
length = len(bomb)

for char in string:
    stack.append(char)
    if char == lastChar and "".join(stack[-length:]) == bomb:
        del stack[-length:]
answer = "".join(stack)

if answer:
    print(answer)
else:
    print("FRULA")