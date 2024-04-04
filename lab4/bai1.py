tong=0
sln=0
while tong<1000:
     a=int(input("nhap so nguyen duong "))
     sln=sln+1
     if a%2!=0:
          print ('so le la:  ',a)
     else :
          print ('so chan la:  ',a)
     tong=tong+a
print ('sóo lượng số nguyên đã nhập là :  ',sln)
