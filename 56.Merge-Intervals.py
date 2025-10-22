def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    arr= [intervals[0]]   
    
    for i in range(1, len(intervals)):
        if intervals[i][0]>arr[-1][1]:
            arr.append(intervals[i])        
        else:
            arr[-1][1]=max(intervals[i][1], arr[-1][1])    
    return arr

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[4,7],[1,4]]))
print(merge([[1,3]]))
print(merge([[1,4],[2,3]]))
print(merge([[1,4],[0,2],[3,5]]))
print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print(merge([[1,10], [2,6], [9,12]]))