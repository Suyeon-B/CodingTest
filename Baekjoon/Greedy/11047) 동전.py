def coin(K, coins):
    answer = 0
    while True:
        if K == 0:
            break
        else:
            share = K//coins[-1]
            answer += share
            K -= share*coins[-1]
            coins.pop()
    return answer

# 입력받기
N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
    if coins[-1] > K:
        coins.pop()
        break
print(int(coin(K, coins)))