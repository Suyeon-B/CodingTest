def solution(prices):
    n = len(prices)
    if n == 1:
        return [1]

    answer = [n-1]*(n-1)+[0]

    for i in range(n-1):
        for j in range(i, n):
            if prices[j] < prices[i]:
                answer[i] = j-i
                break

    return answer


prices = [1, 2, 3, 2, 3] # [5, 4, 1, 2, 1, 0]

print(solution(prices))