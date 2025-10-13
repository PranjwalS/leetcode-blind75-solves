def isPalindrome(s):
    t = ("".join((i.lower() for i in s if i.isalnum())))
    return t==t[::-1]


print(isPalindrome(s = "A man, a plan, a canal: Panama"))
print(isPalindrome(s = "race a car"))