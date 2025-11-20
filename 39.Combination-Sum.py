def combinationSum(candidates, target):   
    def helper(remaining, combo, index):       
        if remaining < 0:
            return
    
        if remaining == 0:
            arr.append(combo.copy())
            return

        for i in range(index, len(candidates)):
            combo.append(candidates[i])
            new_remaining = remaining - candidates[i]       
            helper(new_remaining, combo, i)
            combo.pop()
    
    arr = []
    helper(target, [], 0)    
    return arr
            


candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))