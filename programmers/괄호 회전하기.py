import collections
from copy import deepcopy
def solution(s):
    def pair(bracket):
        bracket = deepcopy(bracket)
        while len(bracket)>1:
            close = bracket.pop()
            if close == '}' and bracket[-1] == '{':
                bracket.pop()
            elif close == ']' and bracket[-1] == '[':
                bracket.pop()
            elif close == ')' and bracket[-1] == '(':
                bracket.pop()
            e
        if len(bracket) == 0:

        return True

    list_s = list(s)
    cnt = 0
    for i in range(len(list_s)):
        temp = list_s.pop(0)
        list_s.append(temp)
        if pair(list_s):
            cnt += 1 

    return cnt

s = "}]()[{"
print(solution(s))