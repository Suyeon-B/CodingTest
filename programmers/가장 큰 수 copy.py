def solution(numbers):
    """
    자리수 비교를 위해 최대공약수 길이 만큼 확장한 뒤, 정렬해서 이어붙인다.
    """
    answer = ''
    strnum = list(map(str, numbers))
    gdb_length = [[i, i * (12//len(i))] for i in strnum]
    gdb_length.sort(key=lambda x:x[1], reverse=True)
    for i in gdb_length: answer += i[0]
    answer = str(int(answer))
    return answer