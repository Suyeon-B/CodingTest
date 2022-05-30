def merge(intervals):
    intervals = sorted(intervals, key=lambda x:x[1])
    intervals = sorted(intervals, key=lambda x:x[0])

    i = 0
    now = intervals[0]
    while i<len(intervals)-1:
        if now[1] >= intervals[i+1][0] and now[1] <= intervals[i+1][1]:
            first,second = now,intervals[i+1]
            new = [now[0], intervals[i+1][1]]
            intervals.remove(first)
            intervals.remove(second)
            intervals.append(new)
            intervals = sorted(intervals, key=lambda x:x[1])
            intervals = sorted(intervals, key=lambda x:x[0])
        elif (now[0] <= intervals[i+1][0] and now[1] >= intervals[i+1][1]):
            intervals.remove(intervals[i+1])
        i+=1
    if len(intervals)>1:
        if intervals[-2][1] >= intervals[-1][0] and intervals[-2][1] <= intervals[-1][1]:
            first,second = intervals[-2],intervals[-1]
            new = [intervals[-2][0], intervals[-1][1]]
            intervals.remove(first)
            intervals.remove(second)
            intervals.append(new)
            intervals = sorted(intervals, key=lambda x:x[1])
            intervals = sorted(intervals, key=lambda x:x[0])
        elif (intervals[-2][0] <= intervals[-1][0] and intervals[-2][1] >= intervals[-1][1]):
            intervals.remove(intervals[-1])

    return intervals


intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals))