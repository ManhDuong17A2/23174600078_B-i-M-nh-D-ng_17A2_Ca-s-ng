a=input('nhap chuoiii:   ')

b=''
c=''
for i in a:
    b=b+i
    if b.isnumeric()==True  :
          c=c+i
    b=''
print (c)
snt=-1
for i in range (2,int(c)):
     if int(c)%i==0:
          snt=-2
          break 
if snt==-1 :
     print ('day la so nguyen to')
else :
     print ('day khong phai so nguyen to ')
