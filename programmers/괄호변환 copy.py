from collections import Counter

def is_correct(p):
    stack = []
    idx = 0
    for idx, bracket in enumerate(p):
        if bracket == ")":
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    return True

def solution(p): # 균형잡힌 괄호 문자열이 주어진다.
    if len(p) == 0:
        return p

    # 문자열 p를 균형잡힌 괄호 문자열 u, v로 분리한다.
    i = 0
    open, close = 0, 0
    for idx, bracket in enumerate(p):
        if bracket == "(":
            open += 1
        else:
            close += 1
        
        if open == close:
            i = idx+1
            break

            
    u, v = p[:i], p[i:]

    
    if is_correct(u): # u가 올바른 괄호 문자열일 때
        return u + solution(v)
    else:# u가 올바른 괄호 문자열이 아닐 때
        temp = "("
        temp += solution(v)
        temp += ")"
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(":
                u = u[:i] + ")" + u[i+1:]
            else:
                u = u[:i] + "(" + u[i+1:]
        return temp + u


p = ")("			 # "()(())()"
print(solution(p))