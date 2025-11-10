from collections import deque
def canFinish(numCourses, prerequisites):
    if not prerequisites:
        return True
    
    n = numCourses
    adjacency_list = [[] for _ in range(n)]
    in_deg =[0]*n

    for i in prerequisites:
        adjacency_list[i[1]].append(i[0])
        in_deg[i[0]]+=1

  
    queue = deque()
    taken = set()
    for i in range(len(in_deg)):
        if in_deg[i] == 0:
            queue.append(i)
            taken.add(i)
    
    while queue:
        prereq = queue.popleft()
        for i in adjacency_list[prereq]:
            in_deg[i]-=1
            if in_deg[i]==0:
                queue.append(i)
                taken.add(i)
        
    return len(taken)==numCourses


numCourses = 6
prerequisites = [[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]] # good
prerequisites2 = [[1,0],[1,2],[3,1],[2,3],[2,4],[4,5],[2,5]] #bad
print(canFinish(numCourses=numCourses, prerequisites=prerequisites))


