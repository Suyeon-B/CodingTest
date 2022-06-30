import math

def factorization(n):
    root_n = math.ceil(math.sqrt(n))
    if root_n > 2:
        for i in range(2, root_n+1):
            if n % i == 0:
                return i, n//i
    else:
        return n, n


def sol(n):
    if n < 3:
        return n
    for i in range(2, math.ceil(math.sqrt(n))):
        answer, n = factorization(n)
        if answer == n:
            print(answer)
            print(n)
            break
        else:
            print(answer)


n = 72
sol(n)