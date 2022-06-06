from collections import deque


def solution(n):
    """
    나머지가 제일 먼저 들어감
    그 다음 몫의 나머지가 들어감
    ...
    몫 < 3일 때 까지 들어감

    3의 배수이면?
    끝에는 무조건 4가 들어감
    다음엔 3이 몇 개 들어가는지 셈 
    """
    answer = ''
    while n:
        if n%3:
            answer += str(n%3)
            n //= 3
        else:
            answer += '4'
            n = n//3-1
    return answer[::-1]

n = 10
print(solution(n))