def reconstructQueue(people):
    result = []
    sorted_by_height = sorted(people, key=lambda x : (-x[0], x[1]))
    for people in sorted_by_height:
        result.insert(people[1], people)

    return result


people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))
        