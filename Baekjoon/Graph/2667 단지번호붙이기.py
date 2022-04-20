"""
조건
1. 집:1 빈곳:0
2. 변을 맞대고 있는 곳을 한 단지로, 단지 개수를 출력하고,
  각 단지에 속하는 집의 수를 오름차순으로 정렬해서 출력
"""

import collections, sys
from collections import deque
sys.stdin = open("Baekjoon/Graph/input.txt",'r')
input = sys.stdin.readline

n = int(input().strip())
houses = []
for i in range(n):
	houses.append(str(input().strip()))

move = [(0,-1),(0,1),(-1, 0),(1,0)] # 상하좌우
visited = [[False]*n for _ in range(n)]
q = deque([])

def bfs(x, y):
	house_cnt = 1
	visited[x][y] = True
	q.append([x,y])
	while q:
		x, y = q.popleft()
		for a, b in move:
			nx, ny = x+a, y+b
			if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
				visited[nx][ny] = True
				if houses[nx][ny] == '1':
					q.append([nx, ny])
					house_cnt+=1
	return house_cnt


cnt = 0
results = []
for i in range(n):
	for j in range(n):
		if houses[i][j] == '1' and not visited[i][j]:
			result = bfs(i, j)
			cnt+=1
			results.append(result)

results.sort()
print(cnt)
print("\n".join(map(str, results)))