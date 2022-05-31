# 투 포인터를 활용한 풀이
# 지금까지의 최대 높이와 현재 높이를 빼서 더해나간다.
def main():
    height = [4, 2, 0, 3, 2, 1]

    if not height:
        return 0

    rain = 0
    left, right = 0, len(height)-1
    max_left, max_right = height[left], height[right]

    while left < right:
        max_left, max_right = max(height[left], max_left), max(
            height[right], max_right)

        # 더 높은 쪽을 향해 투 포인터 이동
        if max_left <= max_right:
            rain += max_left - height[left]
            left += 1
        else:
            rain += max_right - height[right]
            right -= 1
    return rain


print(main())
