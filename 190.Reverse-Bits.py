def reverseBits(n):
    return int(f'{n:032b}'[::-1], 2)
    
print(reverseBits(43261596))
print(reverseBits(2147483644))