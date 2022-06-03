from math import sqrt


def kClosest(points, k):
    def dist(p):
        return sqrt(p[0]**2 + p[1]**2)
    
    output = []
    for point in points:
        output.append([point, dist(point)])
    output.sort(key=lambda x:x[1])
    
    output = output[:k]
    result = []
    for o in output:
        result.append(o[0])
    return result

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points, k))