def numDecodings(s):
    dic = {}
    def helper(i):
        if i == len(s): return 1
        if s[i] == '0': return 0
        if i in dic: return dic[i]
        
        count = helper(i+1)
        if len(s[i:])>=2 and int(s[i: i+2])<=26:
            count += helper(i+2)
        
        dic[i] = count
        return count

    return helper(0), dic





s='22'
print(numDecodings(s))