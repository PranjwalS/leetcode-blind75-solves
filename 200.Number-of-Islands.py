def exist(grid, i, j):
    grid[i][j] = "#"
    rows, cols = len(grid), len(grid[0])

    if i<rows-1 and grid[i+1][j]=="1":
        grid = exist(grid, i+1, j)
    
    if i>0 and grid[i-1][j]=="1":
        grid =  exist(grid, i-1, j)
    
    if j>0 and grid[i][j-1] == "1":
        grid = exist(grid, i, j-1)
    
    if j<cols-1 and grid[i][j+1] == "1":
        grid = exist(grid, i, j+1)
    return grid    
    

def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                grid = exist(grid, i, j)
                count+=1
    return count



grid =[["1"],["1"]]

print(numIslands(grid))