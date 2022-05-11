# 스택으로 다시 풀어보기
def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n

    if n < 2:
        return answer

    for i in range(n-1):
        now = temperatures[i]
        next = temperatures[i+1]
        for j in range(i+1, n-1):
            answer[i] += 1
            if next > now:
                break
            else:
                next = temperatures[j]
                if i+1 == j:
                    next = temperatures[j+1]

    if temperatures[-2] < temperatures[-1]:
        answer[-2] += 1

    return answer


if __name__ == '__main__':
    temperatures = [89,62,70,58,47,47,46,76,100,70]
    print(dailyTemperatures(temperatures))
