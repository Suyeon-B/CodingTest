"""
가능한 경우의 수
1. 끝 계단 직전에서 한 계단 뛰어 온 경우
2. 끝 계단 직전에서 두 계단 뛰어 온 경우
"""
from sys import stdin
stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

n = int(input().strip())
stairs = [int(input().strip()) for _ in range(n)]
if n > 2:
    dp = []
    dp.append(stairs[0])
    dp.append(max(stairs[0]+stairs[1], stairs[1]))
    dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
    for i in range(3, n):
        dp.append(max(dp[i-2] + stairs[i] , dp[i-3] + stairs[i] + stairs[i - 1]))
else:
    if n == 0:
        print(0)
    elif n == 1:
        print(stairs[0])
    else:
        print(max(stairs[0]+stairs[1], stairs[1]))
    exit(0)

print(dp[n-1])
