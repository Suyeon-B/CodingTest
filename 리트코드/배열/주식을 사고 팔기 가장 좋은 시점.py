

import sys


def main():
    prices = [7, 1, 5, 3, 6, 4]

    profit = 0
    now = sys.maxsize
    for price in prices:
        now = min(price, now)
        profit = max(price - now, profit)

    return profit


print(main())

"""
retry
def main():
    prices = [7, 1, 5, 3, 6, 4]

    n = len(prices)
    now = prices[0]
    result = 0
    for i in range(1, n):
        now = min(prices[i], now)
        result = max(prices[i] - now, result)

    return result


print(main())

"""
"""
TLE
def main():
    prices = [7, 1, 5, 3, 6, 4]

    n = len(prices)
    result = 0
    for i in range(n-1):
        now = prices[i]
        later = max(prices[i+1:])
        result = max(later - now, result)

    return result


print(main())

"""
