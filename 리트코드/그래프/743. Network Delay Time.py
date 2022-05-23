import collections
# 플로이드 와샬


def networkDelayTime(times, n, k):
    dist = [[float('inf')]*n for _ in range(n)]

    for time in times:
        dist[time[0]-1][time[1]-1] = time[2]

    for z in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][z] + dist[z][j]:
                    dist[i][j] = dist[i][z] + dist[z][j]
                if i == j:
                    dist[i][j] = 0

    if max(dist[k-1]) == float('inf'):
        return -1
    else:
        return max(dist[k-1])


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))
# 정답 2
