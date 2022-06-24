import itertools
from os import remove


def is_candidate(candidate, relation):
    for r in relation:
        for c in candidate:
            if c not in r:
                return False
            else:
                return True

def solution(relation):
    """
    1. 학번은 무조건 됨
    2. 중복되는지 확인하려면 뽑아서 확인 -> 인덱스로 다 뽑아서 set
    3. 만약 학번 말고 다 중복이 되면 학번 제외 조합해보기
    """
    answer = 1

    # 최소 후보키
    attributes = len(relation[0])
    candidate = []
    for i in range(attributes):
        temp = []
        for j in range(len(relation)):
            temp.append(relation[j][i]) 
        if len(set(temp)) == len(relation):
            candidate.append(i)
    
    # 조합해서 만들어야하는 경우
    # 우선 최소 후보키들 지워줌
    new_cand = list(range(len(relation[0])))
    for c in candidate:
        new_cand.remove(c)

    # 여기까지 [1, 2, 3]

    comb = [new_cand]
    for i in range(2, len(new_cand)):
        temp = list(itertools.combinations(new_cand, i))
        for t in temp:
            comb.append(list(t)) 
    
    # 여기까지 [1, 2, 3, [1, 2], [1, 3], [2, 3]]
    # 다 돌면서 후보키인지 확인
    #    후보키가 맞으면 그게 포함되는 다른 후보들은 지움
    temp = []
    bn_cand = []
    for r in relation:
        for c in comb:
            if len(c)==1:
                temp.append(r[c])
            else:
                for subc in c:
                    temp.append(r[subc])
        if len(temp) == len(relation[0]): # 후보키 찾음
            bn_cand.append(c)

    return bn_cand

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	
# 답 2
print(solution(relation))