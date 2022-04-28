from sys import stdin
stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

n = int(input().strip())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 1. 이전 수+1 해서 온 경우
    if i%3 == 0: # 2. 이전 수//3 으로 온 경우
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0: # 3. 이전 수//2 로 온 경우
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])