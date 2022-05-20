# 그래프 이용한 풀이
# retry 필요
def subsets(nums):
    result = []

    def dfs(index, path):
        # 매 번 결과 추가
        result.append(path)

        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


nums = [1, 2, 3]
print(subsets(nums))
