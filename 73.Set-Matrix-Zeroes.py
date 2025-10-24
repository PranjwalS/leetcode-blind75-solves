def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    m_zero = any(matrix[0][i]==0 for i in range(n))
    n_zero = any(matrix[i][0]==0 for i in range(m))     
     
    for i in range(1, n):
        for j in range(1, m):
            if matrix[j][i] == 0:
                matrix[j][0] = 0
                matrix[0][i] = 0

    for j in range(1, m):
        for i in range(1, n):
            if matrix[j][0] == 0 or matrix[0][i] == 0:
                matrix[j][i] = 0
                
    if m_zero:
        for i in range(n):
            matrix[0][i]=0
            
    if n_zero:
        for i in range(m):
            matrix[i][0] = 0
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))