import math

def bonAppetit(bill, k, b):
    n=len(bill)
    sumC=0
    for i in range(n):
        if(i!=k):
            sumC=sumC+bill[i]
    sumC//=2        
    if(sumC==b):
        print("Bon Appetit")
    else:
        print(b-sumC)

bill=[3,10,2,9]
print(bonAppetit(bill,1,5))