from itertools import combinations_with_replacement


def combinationSum(candidates, target):
    temp = []
    candidates.sort()
    max_len = -(-target//candidates[0])
    for i in range(1, max_len+1):
        for L in list(combinations_with_replacement(candidates, i)):
            if target == sum(L):
                temp.append(list(L))

    return temp


candidates = [2]
target = 1
print(combinationSum(candidates, target))
