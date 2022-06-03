def solution(numbers, target):
    tree = [0]
    for num in numbers:
        sub = []
        for t in tree:
            sub.append(t+num)
            sub.append(t-num)
        tree = sub
    return tree.count(target)

numbers = [4, 1, 2, 1]	
target = 4
print(solution(numbers, target))