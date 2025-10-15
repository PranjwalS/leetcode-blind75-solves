def climbStairs(n):
    a,b=0,1
    for i in range(n+1):
        a,b = b, a+b
    return a


print(climbStairs(0))
print(climbStairs(1))

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(5))