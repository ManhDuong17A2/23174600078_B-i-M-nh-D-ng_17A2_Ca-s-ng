a=int(input('nhap so nguyen :   '))
phannguyen=a//10
b=1
if a==0 or a==1:
        print ('Số chữ số của số nguyên đc nhập vào là: 1')
else :
 while True :
    if a==0 or a==1:
        print ('Số chữ số của số nguyên đc nhập vào là: 1')
       
    b=b+1
    phannguyen=phannguyen//10
    if phannguyen ==0:
        break 

 print ('Số chữ số của số nguyên đc nhập vào là:  ',b) 