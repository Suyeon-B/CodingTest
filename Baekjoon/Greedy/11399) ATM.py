def ATM(N, times_withdraw):
    times_withdraw.sort()
    s = 0
    for i in range(N):
        for j in range(i):
            s += times_withdraw[j]
    s += sum(times_withdraw)
    return s

N = int(input())
times_withdraw = list(map(int, input().split()))
print(ATM(N, times_withdraw))