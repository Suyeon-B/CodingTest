# 메모리 초과 개선 필요
import math
from sys import stdin
stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

"""
dp[i][j] = min(dp[i-j][j-1], dp[i-j][j//3], dp[i-j][j//2])+1
"""
x = int(input().strip())
dp = [[float('inf')]*(int(math.sqrt(2*x))+2) for _ in range(x+1)]
dp[1][0] = 0 # 1은 아무 연산을 하지 않아도 1이다.

for i in range(2, x+1):
    for j in range(1, int(math.sqrt(2*i))+1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j//3], dp[i-j][j//2])+1

result = set(dp[x])
result.remove(float('inf'))
print(max(result))