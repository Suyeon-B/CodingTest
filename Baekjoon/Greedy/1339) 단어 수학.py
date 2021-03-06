def alpha_math(alpha_with_rank):
    points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 자릿값으로 1차 rank 정하기
    sorted_alpha_rank = sorted(alpha_with_rank.items(), key = lambda item: item[1][0], reverse = True)

    alphas = []
    ranks = []

    # 빈도수로 2차 rank 정하기
    freq = []
    for i in range(len(ranks)):
        freq.append(len(ranks[i]))

    # if len(freq) != set(freq):
        

    for i in range(len(sorted_alpha_rank)):
        alphas.append(sorted_alpha_rank[i][0])
        ranks.append(sorted_alpha_rank[i][1])



    answer = 0

    for i in range(len(ranks)):
        point = points.pop()
        for j in range(len(ranks[i])):
            answer += point*(10**(ranks[i][j]-1))

    print(answer)


N = int(input())
if N == 1:
    points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(input())):
        print(points.pop(), end="")
else:
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

    alpha_math(alpha_with_rank)