def countBits(n):
    ans = [0 for i in range(n+1)]
    for i in range(1, len(ans)):
        if i>=1 and i & i-1==0:
            ans[i]=1
        else:
            ans[i] = 1 + ans[i&i-1]          
    return ans


print(countBits(2))
print(countBits(8))