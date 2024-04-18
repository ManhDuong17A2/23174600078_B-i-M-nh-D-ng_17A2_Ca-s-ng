m=int(input("nhap so hang:  "))
n=int(input("nhap so cot: "))
a=[]
for i in range (m):
    a.append([])                       #nhập ma trận a
tong=0
#thêm các giá trị vào ma trận 
for i in range(m):
    for j in range (n):
        l=int(input('nhap:  '))
        a[i].append(l)
        tong=tong+a[i][j]
print ('matran a la: ')
#-------------------------------------------------------------------------------------------------------------
print ('tong ma tran a la: ',tong)      #tính tổng ma trận a 

#-------------------------------------------------------------------------------------------------------------
p=int(input("nhap so hang mtran b:  "))
q=int(input("nhap so cot mtran b: "))
b=[]
for i in range (p):
    b.append([])                        #nhập ma trận b

#thêm các giá trị vào ma trận      
for i in range(p):
    for j in range (q):
        l=int(input('nhap:  '))
        b[i].append(l) 

print ('matran a la:  ') 
print (a)

print ('matran b la:  ')
print (b)


#-------------------------------------------------------------------------------------------------------------
if len(a[1])==len(b): 
 c=[]
 for i in range (m):                 #định dạng ma trận tích 
     c.append([])

 for i in range (m):
    for j in range (q):
       c[i].append(0)

#----------------------------------------------------------------------------------------------------------------    
 for i in range(len(a)):
   for j in range(len(b[1])):
     for k in range(len(b)):        #tích hai ma trận 
       c[i][j] += a[i][k] * b[k][j]
 print ('matran tich la:  ')
 print (c)
else :
   print ('hai ma trận đc nhập không thoa man dieu kien để thụcư hiện nhân ma trận ')

#----------------------------------------------------------------------------------------------------------------
print ('ma tran chuyen vị cua a la: ')
d=[]
for i in range (n):          #định dạng ma trận chuyển vị 
   d.append([])
for i in range (n):               
    for j in range (m):
       d[i].append(0)          

for i in range (len(a)):
   for j in range (len(a[1])):        #ma trận chuyển vị 
      d[j][i]=a[i][j]
print (d)

#----------------------------------------------------------------------------------------------------------------

a=int(input('nhap ma tran vuong cỡ n(nhập n): '))
b=[]
for i in range (a):                           #ma trận vuong cỡ n
    b.append([])
for i in range(a):
    for j in range (a):
          nhap=int(input('nhap cac phan tu : '))
          b[i].append(nhap)
print ('ma tran vuong cỡ n là :  ')   
print (b)
#-----------------------------------------------------------------------
print ('ma tran chuyen vị cua a la: ')
d=[]
for i in range (a):          #định dạng ma trận chuyển vị 
   d.append([])
for i in range (a):               
    for j in range (a):
       d[i].append(0)          

for i in range (len(b)):
   for j in range (len(b[1])):        #ma trận chuyển vị 
      d[j][i]=b[i][j]
print (d)
check=True 
for i in range (len(b)):
    for i in range (len([1])):
        if b[i][j]!=d[i][j]:                               #check ma trận đối xứng 
            check=False 
if check==False :
    print ('day khong phai ma tran doi xung ')
else :
    print ('day la ma tran doi xưng')
    