import math

def sockMerchant(n, ar):
    Arr=[0]*n
    count=0
    for i in range(n):
        for k in range(i+1,n):
            if(ar[i]==ar[k] and Arr[i]==0 and Arr[k]==0):
                Arr[i]=1
                Arr[k]=1
                count=count+1
    return count

Array=[10,20,20,10,10,30,50,10,20]
print(sockMerchant(9,Array))
