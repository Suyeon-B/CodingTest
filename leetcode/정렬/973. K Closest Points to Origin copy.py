def kClosest(points, k):
    points.sort(key=lambda x: x[0]**2+x[1]**2)
    return points[:k]

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points, k))