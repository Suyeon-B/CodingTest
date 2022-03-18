def sugar(N):
    # 3kg, 5kg 설탕의 개수 미지수로 설정하기
    # x : 5kg 설탕의 개수 / y : 3kg 설탕의 개수일 때
    x = N // 5 # 5kg 설탕의 개수
    y = (-5*x + N)/3 # 3kg 설탕의 개수

    # y값이 정수로 떨어지지 않는다면
    if y - int(y) != 0:
        # x의 수를 조절함
        while True:
            if x > 0:
                x -= 1
                y = (-5 * x + N) / 3  # 3kg 설탕의 개수
                if y == int(y):
                    return x+y
            else:
                return -1
    else:
        return x+y

# N값 입력받기
N = int(input())
print(int(sugar(N)))