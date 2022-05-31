def main():
    logs = ["j je", "b fjt", "7 zbr", "m le", "o 33"]

    # 첫 번째 인자를 기준으로 숫자로그, 레터로그 나눠서 배열 저장
    # 레터로그는 알파벳으로 정렬
    # 레터로그부터 output 배열에 append하고 리턴
    letter = []
    digit = []
    for log in logs:
        if log[-1].isalpha():
            letter.append(log)
        else:
            digit.append(log)

    temp = []
    min_idx = float('inf')
    for i in range(len(letter)):
        letter[i] = letter[i].split()
        min_idx = min(min_idx, len(letter[i]))
    for i in range(min_idx-1):
        try:
            letter.sort(key=lambda x: x[i])
        except:
            break
    for i in range(len(letter)):
        try:
            letter[i] = " ".join(letter[i])
        except:
            break

    output = []
    for i in range(len(letter)):
        output.append(letter[i])
    for i in range(len(digit)):
        output.append(digit[i])

    return output


print(main())
