from collections import Counter


def solution(p):
    def is_correct(p):
        temp = []
        for i in range(len(p)):
            if p[i] == "(":
                temp.append(p[i])
            else:
                if not temp:
                    return False
                if temp[-1] == "(":
                    temp.pop()
                else:
                    temp.append(p[i])
        if len(temp) > 0 :
            return False
        else:
            return True
    
    def make_corr(p):
        if len(p) == 0:
            return p

        for i in range(len(p)):
            if not is_correct(p[:i]):
                continue
            else:
                u, v = p[:i], p[i:]
                break
        
        temp = ""
        if is_correct(u):
            return u+make_corr(v)
        else:
            temp += "("
            temp += make_corr(v)
            temp += ")"
            u.popleft()
            u.pop()
            new_u = []
            for i in range(len(u)):
                if u[i] == "(":
                    new_u.append(")")
                else:
                    new_u.append("(")
            return temp + "".join(new_u)


    if len(p) == 0:
        return p

    is_pair = False
    if len(set(Counter(p).values())) == 1: 
        is_pair = True

    if is_pair: # 균형
        if is_correct(p):
            return p
        else:
            return make_corr(p)
    


p = "()))((()" # "()(())()"
print(solution(p))