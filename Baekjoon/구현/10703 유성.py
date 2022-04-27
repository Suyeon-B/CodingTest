from heapq import heappop, heappush
from sys import stdin, stdout

stdin = open("Baekjoon/DP/input.txt",'r')
input = stdin.readline

def main():
    r, s = map(int, input().strip().split())
    photo = [list(input().strip()) for _ in range(r)]

    # 유성, 땅의 좌표
    meteors = []
    min_dist = float('inf')
    for i in range(r):
        for j in range(s):
            if photo[i][j] == 'X':
                heappush(meteors, [-i, j])
                x = i
                temp = 0
                while True:
                    x += 1 # 한 칸씩 아래로 내려보며 땅과의 거리의 최솟값 구하기
                    if photo[x][j] == '#':
                        min_dist = min(temp, min_dist)
                        break
                    elif photo[x][j] == 'X':
                        break
                    temp += 1
    
    # 최소 거리만큼 유성을 떨어뜨려 배치함
    for i in range(len(meteors)):
        x, y = heappop(meteors)
        x = -x
        photo[x][y] = '.'
        photo[x+min_dist][y] = 'X'

    for i in range(r):
        stdout.write("".join(photo[i]))
        stdout.write('\n')
main()