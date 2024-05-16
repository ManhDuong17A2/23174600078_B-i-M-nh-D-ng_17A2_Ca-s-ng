def sumPdivisors(n):
    tong=0
    for i in range (1,n):
        if n%i==0:
            tong=tong +i

    return tong
def kiemtra(a,b):
    if sumPdivisors(a)==b and sumPdivisors(b)==a:
        return True 
    else :
        return False 
print (kiemtra (220,284))

