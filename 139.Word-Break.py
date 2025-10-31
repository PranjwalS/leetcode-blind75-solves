def wordBreak(s, wordDict):
    dic = {}   
    def helper(i):
        if i in dic: return dic[i]
        if i == len(s):
            return True
        
        for j in range(i+1, len(s)+1):  
            if s[i:j] in wordDict:
                if helper(j):
                    return True  
            
        dic[i] = False
        return False 

    return helper(0)


s = "abcd"
wordDict = ["a","abc","b","cd"]
print(wordBreak(s, wordDict))