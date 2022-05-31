# 그래프 풀이
def letterCombinations(digits):
    def dfs(index, path):
        # 글자수 만큼 dfs 탐색
        if len(path) == len(digits):
            result.append(path)
            return
        
        # 입력값 자릿수 단위 반복
        for i in range(index,len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i+1, path+j)
    
    # 예외처리
    if not digits:
        return []
    
    dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result=[]
    dfs(0,"")

    return result

digits = "23"
print(letterCombinations(digits))