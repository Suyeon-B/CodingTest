# enumerate & stack
def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            last = stack.pop()
            answer[last] = i-last
        stack.append(i)
    return answer


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temperatures))
