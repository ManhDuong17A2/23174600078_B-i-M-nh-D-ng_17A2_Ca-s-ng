a=input("nhap chuoi van ban:  ")
b=input('nhap tu muon tim kiem:  ')
i=len(a)
h=a.count(a)

print ('tu cần tìm kiếm xuất hiện ở các vị trí trong chuỗi: ')
while True :
    k=a.rfind(b,0,i)
    i=int(k)-1
    if k==-1:
        break
    print (k,end=',')
max=0
kitumax=''
for i in a:
    k=a.count(str(i))
    if k>=max:
        max=k
        kitumax=i
 

print ('\n ki tu xuat hien nhieu nhat la:',kitumax)


