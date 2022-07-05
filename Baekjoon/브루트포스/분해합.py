"""
245의 분해합은 256(= 245 + 2 + 4 + 5)
따라서 245는 256의 생성자

가장 작은 생성자 구하기
"""

from sys import stdin

stdin = open("input.txt",'r')
input = stdin.readlines
curr = input()[0]
curr_list = list(curr)
for i in range(len(curr_list)):
    curr_list[i] = int(curr_list[i])

SUM = 0
curr = int(curr) - sum(curr_list)
while SUM != curr:
    for c in str(curr):
        SUM += int(c)
    curr -= 1

print(curr)

