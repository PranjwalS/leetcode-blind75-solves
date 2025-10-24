def uniquePaths(m,n):
    # mfact, nfact, numfact = (1,1,1)
    # for i in range(1, m):
    #     mfact*=i
    # for i in range(1, n):
    #     nfact*=i
    # for i in range(1, (n-1)+(m-1)+1):
    #     numfact*=i
    # return int(numfact/(mfact*nfact))
    
    # arr = [[0]*n for _ in range(m)]
    # for i in range(n):
    #     arr[0][i]=1
    # for i in range(m):
    #     arr[i][0]=1
    # for i in range(1,n):
    #     for j in range(1,m):
    #         arr[j][i] = arr[j-1][i]+arr[j][i-1]
    # return arr[-1][-1]
            
            
    arr = [1]*m
    for i in range(1,n):
        for j in range(1,m):
            arr[j]+=arr[j-1]
    return arr[-1]

    
    
    
    
     
print(uniquePaths(3,7)) 
print(uniquePaths(1,1))