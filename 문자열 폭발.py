"""
시간초과 개선 필요
1. 폭발 문자열이 포함되면 해당 문자열 삭제
2. 삭제한 새로운 문자열에 폭발 문자열이 포함되면 1번으로 돌아감

-> 모든 폭발이 끝나고 남은 문자열 출력
(없으면 'FRULA' 출력)

(폭발 문자열은 같은 문자 포함 X)
"""
from sys import stdin

stdin = open("input.txt",'r')
input = stdin.readline

string = input().strip()
bomb = input().strip()

while string and bomb in string:
    string = string.replace(bomb, "")

if string:
    print(string)
else:
    print("FRULA")