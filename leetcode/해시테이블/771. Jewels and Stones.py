def numJewelsInStones(jewels, stones):
    cnt = 0
    for st in stones:
        if st in jewels:
            cnt += 1
    return cnt


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
