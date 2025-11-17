def getSum(a, b):
    mask = 0xFFFFFFFF
    xor = (a^b) & mask
    inter = (a&b) & mask
    while inter>0:
        inter = (inter << 1) & mask
        xor, inter = (xor^inter)&mask,(xor&inter)&mask
  
    return xor if xor <= 0x7FFFFFFF else ~(xor^mask)


print(getSum(1, 2)) # 3
print(getSum(2,3)) # 5
print(getSum(-1,11))