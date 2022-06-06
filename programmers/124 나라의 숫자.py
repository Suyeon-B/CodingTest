from collections import deque


def solution(n):
    answer = deque([])
    first = True
    if n%3 != 0: # 3의 배수가 아니면
        while(n>3):
            if first:
                first = False
                answer.appendleft(n%3)
                n = n-n//3
            else:
                answer.appendleft(n%3)
                n = n-n//3
    # else:
        

    
    return answer

n = 10
print(solution(n))