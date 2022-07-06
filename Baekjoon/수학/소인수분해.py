def factorization(n):
    d = 2

    while d <= n:
        if n%d == 0:
            print(d)
            n = n//d
        else:
            d += 1

n = int(input())
factorization(n)