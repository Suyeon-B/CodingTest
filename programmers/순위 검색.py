def solution(info, query):
    # 문자열 파싱
    for i in range(len(info)):
        info[i] = info[i].split(" ")
        query[i] = query[i].split(" and ")
        query[i][-1] = query[i][-1].split(" ")
        query[i] = query[i][:-1] + query[i][-1]

    flag = True
    answer = []
    cnt = 0
    for q in query: # 조건 쿼리중 하나
        for i in info:
            if int(i[-1]) < int(q[-1]):
                flag = False
                # break
            else:
                for idx in range(4): # 지원자
                    if q[idx] == '-':
                        continue
                    else:
                        if i[idx] != q[idx]:
                            flag = False
                            break
            if flag:
                cnt += 1
            flag = True
        answer.append(cnt)
        cnt = 0

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	
print(solution(info, query))