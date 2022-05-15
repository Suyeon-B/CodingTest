import collections
def numIslands(grid):
    move = [(0,-1),(0,1),(-1, 0),(1,0)] # 상하좌우
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    q = collections.deque([])

    def bfs(x, y):
        house_cnt = 1
        visited[x][y] = True
        q.append([x,y])
        while q:
            x, y = q.popleft()
            for a, b in move:
                nx, ny = x+a, y+b
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == '1':
                        q.append([nx, ny])
                        house_cnt+=1
        return house_cnt


    cnt = 0
    results = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and not visited[i][j]:
                result = bfs(i, j)
                cnt+=1
                results.append(result)
    return cnt

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))