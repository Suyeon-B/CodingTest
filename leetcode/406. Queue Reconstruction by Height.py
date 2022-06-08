def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0], x[1])) # 이거 쩐다!!
    queue = []
    for p in people:
        queue.insert(p[1], p) # 이 부분이 핵심
    return queue


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))
        