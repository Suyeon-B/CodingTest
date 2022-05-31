import itertools


def combine(n, k):
    return [list(comb) for comb in itertools.combinations(range(1, n+1), k)]


n = 4
k = 2
print(combine(n, k))
