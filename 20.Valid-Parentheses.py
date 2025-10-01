class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"} 

        for i in s:
            if i in mapping:
                if stack==[] or stack.pop() != mapping[i]:
                    return False
            else:
                stack.append(i)    
        return True if stack==[] else False
    
sol = Solution()
s = "()[]{}"
s2 = "()"
s3= "[([]])"
s4 = "([)]"
s5 = ")"


print(sol.isValid(s))
print(sol.isValid(s2))
print(sol.isValid(s3))
print(sol.isValid(s4))
print(sol.isValid(s5))

