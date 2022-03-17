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



#     # N이 5나 3의 배수일 때
#     # 3의 배수인지 미리 구해 변수로 저장
#     mul3_N = is_3mul(N)
#     mul3_y = is_3mul(N-(5*x))
#     mul3_x = is_3mul(x)
#
#     if mul3_N is True: # N이 3의 배수일 때
#         if mul3_y is False:
#             return N//3
#         else:
#             return x+y
#     elif N%5 == 0: # N이 5의 배수일 때
#         return x
#
#     # N이 5과 3의 공배수일 때
#     if mul3_N is True: # N이 3의 배수일 때
#         if mul3_x is True: # x가 3의 배수면
#             if y < 0:
#                 return -1
#             else:
#                 return x+y
#         else: # x가 3의 배수가 아니면
#             return -1
#     else: # N이 3의 배수가 아닐 때
#         if mul3_x is True: # x가 3의 배수면
#             return -1
#         else: # x가 3의 배수가 아니면
#             if y < 0:
#                 return -1
#             else:
#                 return x+y
#
#
# def is_3mul(n):
#     temp = n
#     digits = []
#     while True:
#         if temp < 10:
#             digits.append(temp)
#             break
#         else:
#             R = temp%10
#             temp //= 10
#             digits.append(R)
#
#     sum = 0
#     for i in range(len(digits)):
#         sum += digits[i]
#
#     if sum%3 == 0:
#         return True
#     else:
#         return False

# N값 입력받기
N = int(input())
print(int(sugar(N)))