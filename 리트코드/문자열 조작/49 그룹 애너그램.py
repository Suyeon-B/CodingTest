"""
IDEA
- 정렬 후 같은 문자끼리 새로운 리스트에 담는다.
"""
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

# 들어온 문자열이 없을 때 예외처리
if len(strs) == 1:
    print('[[""]]')
    exit(0)

# 우선 모든 문자를 set으로 받아 정렬한 값을 value로 딕셔너리에 넣는다.
sorted_strs=[]
for i in range(len(strs)):
    sorted_strs.append("".join(sorted(strs[i])))

dict = {}
for i in range(len(strs)):
    dict[strs[i]] = "".join(sorted(strs[i]))


# value값이 일치하면 한 묶음으로 넣는다.
answers = [[] for i in range(len(set(sorted_strs)))]
now = 0
check = [False]*len(strs)
answers[0].append(strs[now])
check[0] = True
idx = 0

next = 1
while True:
    for i in range(next, len(strs)):
        if dict[strs[now]] == dict[strs[i]] and not check[i]:
            answers[idx].append(strs[i])
            check[i] = True
        else:
            if next == now+1 and not check[i]:
                next = i
    if next == len(strs)-1:
        for answer in answers:
            if answer:
                if dict[answer[0]] == dict[strs[-1]]:
                    answer.append(str[-1])
                    check[-1] = True
            else:
                answer.append(strs[-1])
                check[-1] = True
    if len(set(check))==1:
        print(answers)
        exit(0)
    idx += 1
    now = next
    answers[idx].append(strs[now])
    check[next] = True
    next = now+1