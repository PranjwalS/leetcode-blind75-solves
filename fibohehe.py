def fibo():
    a = 1 
    b = 1
    arr = [1]
    exp = []
    i = 1
    x=0
    while x<100:
        b, a = b+a, b
        arr += [a]
        exp.append(2**i)
        i+=1
        x+=1
    return 2**3200000
    # return arr[-1] if arr[-1] > exp[-1] else exp[-1]

print(fibo())