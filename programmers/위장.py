import collections
def solution(clothes):
    answer = 1
    dict = collections.defaultdict(list)
    for c in clothes:
        dict[c[1]].append(c[0])
    v = list(dict.values())
    for i in range(len(v)):
        answer *= (len(v[i])+1)
    
    return answer-1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))