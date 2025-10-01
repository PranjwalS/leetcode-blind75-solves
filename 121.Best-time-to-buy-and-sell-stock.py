
                
         
def maxProfit(prices):
    dif = 0
    minp = float('inf')
    for price in prices:
        if minp>price:
            minp=price
        elif price-minp>dif:
            dif = price-minp
    return dif
            
               




l1=[7,1,5,3,6,4]
l2=[7,6,5,3,1]
print(maxProfit(l1))
print(maxProfit(l2))