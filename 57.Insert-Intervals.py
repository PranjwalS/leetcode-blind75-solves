def insert(intervals, newInterval):
    l,r = [], []
    for interval in intervals:
        if newInterval[1]<interval[0]:
            r.append(interval)
        elif interval[1]<newInterval[0]:
            l.append(interval)
        else:
            newInterval[0], newInterval[1] = min(newInterval[0], interval[0]), max(interval[1], newInterval[1])
    return l + [newInterval] + r



print(insert([[1,3],[6,9]], [2,5]))
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16], [18,20]], [4,8]))