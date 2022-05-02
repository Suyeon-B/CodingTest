# TLE
def main():
    height = [5, 4, 1, 2]
    size = len(height)
    rain = [0] * size
    result = 0
    trigger = False
    while sum(height) > 1:
        for i in range(size):
            if height[i] > 0:
                rain[i] = 1
                height[i] -= 1
        for j in range(size-1):
            if rain[j] > 0 and not trigger:
                trigger = True
            if rain[j] == 0 and trigger and sum(rain[j:]) > 0:
                result += 1
        rain = [0] * size
        trigger = False
    return result


print(main())
