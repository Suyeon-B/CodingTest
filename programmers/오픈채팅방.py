from collections import defaultdict

def solution(record):
    record = [list(r.split(" ")) for r in record]
    dict = defaultdict(list)
    answer = []
    for r in record: # key=id value=[닉네임]
        if r[0] == 'Enter':
            answer.append(['Enter', r[1]])
            dict[r[1]] = r[2]
        elif r[0] == 'Leave':
            answer.append(['Leave', r[1]])
        else:
            dict[r[1]] = r[2]
    
    output = []
    temp = ""
    for a in answer:
        if a[0] == 'Enter':
            temp += str(dict[a[1]])
            temp += "님이 들어왔습니다."
            output.append(temp)
            temp = ""
        else:
            temp += str(dict[a[1]])
            temp += "님이 나갔습니다."
            output.append(temp)
            temp = ""

    return output

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
print(solution(record))