from curses.ascii import isdigit
from sys import stdin

stdin = open("Baekjoon/문자열/input.txt",'r')
input = stdin.readline

length = int(input().strip())
string = input().strip()

number = ""
answer = 0
for i in range(length):
    if isdigit(string[i]):
        number+=string[i]
    elif number:
        answer += int(number)
        number = ""
    # 숫자로만 이루어진 경우
    if i == length-1 and number:
        answer += int(number)

print(answer)