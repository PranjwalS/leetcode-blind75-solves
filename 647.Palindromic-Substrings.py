def countSubstrings(s):
    working = list(s)
    for center in range(1, len(working)-1):
        left = center-1
        right = center+1
        
        while s[center:right+1] == s[center:left-1:-1]:
            working.append(s[left: right+1])
            left-=1
            right+=1
    
    return working




print(countSubstrings("racecar")) #3
print(countSubstrings('aaa')) #6