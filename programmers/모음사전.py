import itertools
def solution(word):
    answer=[]
    for i in range(1, 6):
        comb = list(itertools.product(['A', 'E', 'I', 'O', 'U'], repeat=i))
        answer+=[''.join(c) for c in comb]
    
    answer.sort()
    return answer.index(word)+1

word = "AAAAE"
print(solution(word))