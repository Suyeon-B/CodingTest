from sys import stdin
stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

"""
dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
"""

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    dp = [[0, 0]] * (n+1)
    for i in range(n+1):
        if i == 0:
            dp[i] = [1, 0]
        elif i == 1:
            dp[i] = [0, 1]
        else:
            dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
    print(" ".join(map(str, dp[n])))