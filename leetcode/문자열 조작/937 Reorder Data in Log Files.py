def main():
    logs = ["j je", "b fjt", "7 zbr", "m le", "o 33"]

    # 첫 번째 인자를 기준으로 숫자로그, 레터로그 나눠서 배열 저장
    # 레터로그는 알파벳으로 정렬
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다 표현식으로 정렬
    letters = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))
    return letters+digits


print(main())
