"""
핵심 IDEA 
- 우선순위 기준 : 10^{자릿수} * 빈도수 
"""
import operator
import sys, collections # defaultdict, Counter import
sys.stdin = open("Baekjoon/Greedy/input.txt",'r')
input = sys.stdin.readline

n = int(input().strip())
strings = []

temp = ''
for i in range(n):
    string = input().strip()
    strings.append(string)

    # 문자열을 세어주는 용도로 string을 합쳐준다.
    temp += string

# 입력된 문자열의 빈도수를 세어준다.
freq = collections.Counter(temp)

# 입력된 문자열의 자릿수 중 최댓값을 계산한다.
digit = collections.defaultdict(int)
for string in strings:
    for chr in string:
        idx = len(string) - string.index(chr) - 1
        if not digit[chr]:
            digit[chr] = idx
        else:
            digit[chr] = max(idx, digit[chr])

# dict[문자] = (우선순위) 형태로 저장한다.
# 우선순위 기준 : 10^{자릿수} * 빈도수
priority = collections.defaultdict(int)
for chr in digit.keys():
    priority[chr] = 10**digit[chr] * freq[chr]

# 우선순위로 sort
priority = dict(sorted(priority.items(), key=operator.itemgetter(1), reverse=True))

# 우선순위값을 기준으로 9~0까지 할당
chrs = priority.keys()
points = collections.defaultdict(int)
p = 9
for chr in chrs:
    points[chr] = p
    p-=1

# 합 계산
total = 0
for string in strings:
    for chr in string:
        total += 10**(len(string) - string.index(chr) - 1) * points[chr]
        string = string[1:]

print(total)