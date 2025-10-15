def productExceptSelf(arr):
    lst = [1]*len(arr)
    left = [1]*len(arr)
    right = [1]*len(arr)
   
    for i in range(1, len(arr)):
        left[i] = (arr[i-1]*left[i-1])
        
        
    for i in range(len(arr)-2, -1, -1 ):
        right[i] = (arr[i+1]*right[i+1])
        lst[i] = left[i]*right[i]
    lst[-1] = left[-1]*right[-1]
    return lst
                
            

print(productExceptSelf([1,2,3,4]))
# print(productExceptSelf([-1,1,0,-3,3]))