

def sugar(N):
    # 3kg, 5kg 설탕의 개수 미지수로 설정하기
    x = N//3
    y = x//5

    if x == 0 and y == 0:
        return -1

    # x값이 3의 배수인지 판별하기
    x_copy = y
    x_list = []
    while True:
        if x_copy < 10:
            x_list.append(x_copy)
            break
        else:
            x_list.append(x_copy // 10)
    sum = 0
    for i in range(len(x_list)):
        sum += x_list[i]

    if sum%3 != 0:
        return(-1)

    if y>0:
        if N<5:
            return(-1)

    return x+y

# N값 입력받기
N = int(input())
print(sugar(N))