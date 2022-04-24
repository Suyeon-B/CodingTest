import collections, sys
from collections import deque
sys.stdin = open("Baekjoon/Graph/input.txt",'r')
input = sys.stdin.readline

# 테스트 케이스의 개수
t = int(input().strip())

# 가로m 세로n 배추 개수k
m, n, k = map(int, input().strip().split())
move = [(0,-1),(0,1),(-1, 0),(1,0)] # 상하좌우

def bfs(x, y):
    q = deque(())
    visited[x][y] = True
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for a, b in move:
            nx, ny = x+a, y+b
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == '1':
                    q.append([nx, ny])


for _ in range(t):
    graph = collections.defaultdict(list)
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(k):
        x, y = map(int, input().strip().split())
        graph[x][y] = 1 # 배추 위치 표시

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt+=1

    print(cnt)
