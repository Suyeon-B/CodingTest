def validUtf8(data):
    """
    앞에 1개수-1만큼 
    뒤의 2진수가 10으로 시작해야함
    """
    # 2진수 변환
    for i in range(len(data)):
        data[i] = bin(data[i])[2:].zfill(8)
    
    # 1개만 들어온 경우
    if len(data) == 1:
        if data[0][0] == '0':
            return True
        else:
            return False

    # 앞의 1개수
    cnt = 0
    for num in data[0]:
        if num == '1':
            cnt+=1
        else:
            break

    # 돌면서 확인
    for i in range(1, len(data)):
        cnt -= 1
        if cnt>0 and (data[i][0] != '1' or data[i][1] != '0'):
            return False
        if cnt == 0:
            if data[i][0] != '0':
                return False

    if cnt < 2:
        return True
    else:
        return False

data = [250,145,145,145,145]
print(validUtf8(data))