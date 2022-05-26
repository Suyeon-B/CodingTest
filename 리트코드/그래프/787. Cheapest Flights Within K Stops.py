from os import remove


def findCheapestPrice(n, flights, src, dst, k):
    dist = [[float('inf')]*n for _ in range(n)]
    t = [[k]*n for _ in range(n)]

    for f in flights:
        dist[f[0]][f[1]] = f[2]

    for z in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][z] + dist[z][j] and i != src:# and t[src][dst]:
                    t[i][j] -= 1
                    dist[i][j] = dist[i][z] + dist[z][j]
                if i == j:
                    dist[i][j] = 0

    if dist[src][dst] < float('inf'):
        return dist[src][dst]
    else:
        return -1


n = 4
flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))
