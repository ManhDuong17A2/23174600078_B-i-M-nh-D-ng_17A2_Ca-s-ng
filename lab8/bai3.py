def cubesum(n):
    k=[]
    for i in n :
        k.append(int(i))
    h=[i**3  for i in k]
    tong=0
    for i in h:
        tong=tong+i
    return tong
a=input('nhap mot so :'  )
print (cubesum(a))


def PrintArmstrong(l):
    if cubesum(l)==int(l):
        print('in ra so armstrong :',l)
def isArmstrong(d):
    if cubesum(d)==int(d):
        return 'day la so armstrong :' ,True
    else :
        return 'day la so armstrong :', False
print (PrintArmstrong(a))
print(isArmstrong(a))

