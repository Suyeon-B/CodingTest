from sys import stdin

stdin = open("Baekjoon/수학/input.txt",'r')
input = stdin.readline

n = input().strip()

if n[0] == '0':
    if len(n)>1 and n[1] == 'x': # 16진수
        print(int(n, 16))
    else:
        print(int(n, 8))
else:
    print(n)