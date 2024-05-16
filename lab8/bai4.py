def sumPdivisors(n):
    tong=0
    for i in range (1,n):
        if n%i==0:
            tong=tong +i

    return tong

print (sumPdivisors(32))
