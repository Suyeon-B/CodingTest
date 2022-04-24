import sys
sys.stdin = open("Baekjoon/Greedy/input.txt",'r')
input = sys.stdin.readline

n = int(input())
cost = list(map(int, input().strip().split()))
juyouso = list(map(int, input().strip().split()))

min_sofar = juyouso[0]
MIN = min(juyouso[:-1])
result = 0
for i in range(n):
    if juyouso[i] == MIN:
        result += MIN*sum(cost[i:])
        break
    elif juyouso[i] >= min_sofar:
        result += min_sofar*cost[i]
    elif juyouso[i] < min_sofar:
        min_sofar = juyouso[i]
        result += min_sofar*cost[i]

print(result)