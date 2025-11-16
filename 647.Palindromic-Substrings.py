def countSubstrings(s):
    count=0
    for center in range(len(s)):
        for left, right in [(center, center), (center, center+1)]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left -= 1
                right += 1    
    return count




print(countSubstrings("racecar")) #3
print(countSubstrings('aaa')) #6
print(countSubstrings('abbcc')) #6
print(countSubstrings('abc')) #6