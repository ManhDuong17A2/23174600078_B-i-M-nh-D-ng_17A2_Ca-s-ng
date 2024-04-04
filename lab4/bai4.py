n=int(input("nhap so n:  "))
if n>10:
 a=0
 S1=0
 S2=1/3
 S3=0
 S4=0
 while a<n:
     a=a+1 
     S1=S1+(6**a)
     S2=S2+(1/(3**(2*a+1)))
     S3=S3+((-1)**a)*(a**2)
     S4=S4+(a*(a+1)*(a+2))
    
 print ("Tổng S1 là:  ",S1)
 print ("Tổng S2 là:  ",S2)
 print ("Tổng S3 là:  ",S3)
 print ("Tổng S4 là:  ",S4)
else:
   print ("nhâp n lớn hơn 10")