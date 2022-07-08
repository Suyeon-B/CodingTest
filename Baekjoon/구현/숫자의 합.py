from sys import stdin

stdin = open("Baekjoon/구현/input.txt",'r')
input = stdin.readline

n = int(input().strip())
numbers = input()
numbers_list = [int(num) for num in numbers]

print(sum(numbers_list))