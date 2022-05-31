import itertools
def solution(numbers):
    """
    1. 숫자 갯수만큼 순열 뽑고
    2. join으로 합쳐서 int로 만든 다음에
    3. max값 str변환 후 리턴
    """
    permut = list(itertools.permutations(numbers, len(numbers)))
    answer = sorted([''.join(map(str, p)) for p in permut], reverse= True)
    return answer[0]

numbers = [6, 10, 2]
print(solution(numbers))