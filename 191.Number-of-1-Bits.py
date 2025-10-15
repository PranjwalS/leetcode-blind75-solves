def hammingWeight(n):
    x=0
    for i in bin(n):
        x += 1 if i=="1" else 0
    return x

print(hammingWeight(11))