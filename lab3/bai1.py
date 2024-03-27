n= int ( input(' nhap so nguye duong n:  '))
if n<=0:
    print ("hãy nhập lại, nhập sóo nguyên dương.")
else :
    S1=0
    for i in range (1,n+1):
        S1=S1+i 
    print ("tổng S1 là :", S1)

    #-----------------------------
    S2=0
    for i in range (1,n+1):
        phanso=1/i
        S2=S2+phanso
    print ('Tổng S2 là :',S2)

    #-----------------------------
    S3=0
    for i in range (1,n+1):
        if i%2==0:
         phansocan=1/((i)**(1/2))
         S3=S3+phansocan
    print ("Tổng S3 là: ",S3)

    #-----------------------------
    S4=0
    for i in range (1,n+1):
        phansomu=((-1)**(i+1))/i
        S4=S4+phansomu
    print ('Tổng S4 là :', S4)


