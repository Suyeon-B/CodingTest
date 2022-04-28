# 메모리 초과
from sys import stdin
stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

# 보석 개수 n, 가방 개수 b
n, b = map(int, input().strip().split())

# 보석의 무게와 가치, 가성비를 담아줄 배열
value = []
for _ in range(n):
    m, v = map(int, input().strip().split())
    cp = v//m
    value.append([m, v, cp])


# 무게가 무거운 것으로 정렬
value = sorted(value, key=lambda x:x[0])
# 가성비가 큰 보석을 먼저 담아야 하므로, 정렬
value = [[0, 0, 0]] + sorted(value, key=lambda x:x[2], reverse=True)

# 가방에 담을 수 있는 최대 무게
weight = []
for _ in range(b):
    weight.append(int(input().strip()))
# 큰 가방부터 채우도록 정렬
weight = sorted(weight, reverse=True)


result = 0
idx = 0
for k in range(b):
    # 보석의 최대 누적 가치를 담아줄 배열
    value_sofar = [[0]*(weight[k]+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, weight[k]+1):
            # 물건의 무게와 가치 (w, v)
            w, v = value[i][0], value[i][1]
            if j < w: # 현재 허용된 무게보다 넣으려는 물건의 무게가 더 무겁다면
                value_sofar[i][j] = value_sofar[i-1][j] # 넣지 않는다. (직전 무게와 동일)
            else: # 현재 허용된 무게 안에 드는 무게라면
                # 1. 현재 물건을 넣는다.
                # 2. 현재 물건을 넣지 말고 이전 배낭 그대로 가지고 간다.
                # 위 둘 중 가치가 큰걸 선택한다.
                if v > value_sofar[i-1][j]:
                    value_sofar[i][j] = v
                    idx = i
                else:
                    value_sofar[i][j] = value_sofar[i-1][j]
                    idx = i-1
    result += value[idx][1]
    value[idx] = [0, 0, 0]
    

print(result)