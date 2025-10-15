def isAnagram(s,t):
    # return sorted(s)==sorted(t)

    # sdic = {}
    # for key in s:
    #     if key in sdic:
    #         sdic[key]+=1
    #     else:
    #         sdic[key]=1
    
    # for key in t:
    #     if key in sdic:
    #         sdic[key]-=1
    #         if sdic[key]==0:
    #             del sdic[key]
    #     else:
    #         return False
            
    #fastest        
    alls = [0]*26
    allt = [0]*26
    for char in s:
        alls[ord(char)-ord('a')]+=1
    for char in t:
        allt[ord(char)-ord('a')]+=1
    
    return alls==allt
    
    
print(isAnagram("anagram" ,"nagaram"))
print(isAnagram("rat", "car"))