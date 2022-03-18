def alpha_math(alpha_with_rank):
    points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sorted_alpha_rank = sorted(alpha_with_rank.items(), key = lambda item: item[1][0], reverse = True)

    alphas = []
    ranks = []

    for i in range(len(sorted_alpha_rank)):
        alphas.append(sorted_alpha_rank[i][0])
        ranks.append(sorted_alpha_rank[i][1])

    answer = 0

    for i in range(len(ranks)):
        point = points.pop()
        for j in range(len(ranks[i])):
            answer += point*(10**(ranks[i][j]-1))

    return answer



N = int(input())
alpha_with_rank = {}
digit_sum = 0
for i in range(N):
    alpha = input()
    alpha_digit = len(alpha)
    digit_sum += alpha_digit
    for j in range(alpha_digit):
        if alpha[j] in alpha_with_rank:
            alpha_with_rank[alpha[j]].append(alpha_digit - j)
            alpha_with_rank[alpha[j]].sort(reverse=True)
        else:
            alpha_with_rank[alpha[j]] = [alpha_digit - j]


print(alpha_math(alpha_with_rank))