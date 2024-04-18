a=int(input('nhap n : '))
b=[int(input("nhap cac so: ")) for i in range(a)]
#=============================================================
daysnt=[]
for i in b:
    sothuong=100

    for j in range (2,i):
       if i%j==0:
           sothuong=i
           break
    if i!=sothuong:
        daysnt.append(i)
print ('cac so nguyen to trong mang la:',daysnt)
#=============================================================
dayshh=[]
for i in b:
    tong=0
    for j in range (1,i):
       if i%j==0:
           tong=tong+j    
    if tong==i:
        dayshh.append(i)
print ('cac so hoan hao trong mang la: ',dayshh)

