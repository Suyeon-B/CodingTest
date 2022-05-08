def solution(atmos):
    mask, day = 0, 0
    mask_on = False

    for i in range(len(atmos)):
        if mask_on:
            day += 1
        # 이틀 후 까지만 재사용
        if day >= 3:
            day = 0
            mask_on = False
        # 나쁨 이상
        if (atmos[i][0] >= 81 and atmos[i][0] < 151) or (atmos[i][1] >= 36 and atmos[i][1] < 76):
            if not mask_on:
                mask += 1
                mask_on = True
        # 둘 다 매우나쁨
        if (atmos[i][0] >= 151 and atmos[i][1] >= 76):
            if not mask_on:
                mask += 1
            mask_on = False
            day = 1

    return mask


atmos = [[80, 35], [70, 38], [100, 41], [75, 30],
         [160, 80], [77, 29], [181, 68], [151, 76]]
print(solution(atmos))
