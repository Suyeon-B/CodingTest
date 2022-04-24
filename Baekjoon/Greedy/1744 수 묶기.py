"""
IDEA
1. 입력 값 정렬해서 맨 앞의 값이 양수면, 우선 젤 끝 큰 애들끼리 묶음
2. 맨 앞이 음수면, 다음 최솟값이랑 묶음
3. max(1번 값, 2번 값) 출력
"""
import collections, sys
sys.stdin = open("Baekjoon/Greedy/input.txt",'r')
input = sys.stdin.readline

# 수열의 크기 n
n = int(input().strip())

# 입력값이 하나면 바로 출력 후 종료
if n == 1:
    print(input().strip())
    exit(0)

numbers = []
for i in range(n):
    numbers.append(int(input().strip()))


numbers.sort()
candidate = []
if numbers[0] < 0:
    temp = numbers[0]*numbers[1] + sum(numbers[1:])
    candidate.append(temp)
if numbers[0] == 0:
    candidate.append(sum(numbers))
temp = numbers[-1]*numbers[-2] + sum(numbers[:-2])
candidate.append(temp)

print(max(candidate))