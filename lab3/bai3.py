
print ('Các số nguyên tố 100-1000: ')
for i in range (100,1001):
    sothuong=100

    for j in range (2,i):
       if i%j==0:
           sothuong=i
           break
    if i!=sothuong:
        print (i,end=",")

#------------------------------------------
print ('\n Các số chính phương từ 1-1000: ')
for i in range (1,1001):
    sochinhphuong=100

    for j in range (1,i):
       if (i**(1/2))%j==0:
           sochinhphuong=i
           break
       
    if i==sochinhphuong:
        print (i,end=',')

#-------------------------------------------
a=0
b=1
print ("\n Dãy fibonanci có số cuối nhỏ hơn 100 là: ")
for i in range (1,101):
    if i==1:
        print ('0,1')
    c=a+b
    a=b
    b=c
    if c>=100:
        break
   
    print (c,end=',')
   
#-------------------------------------------
print ('\n Các số hoàn hảo nhỏ hơn 100: ')
for i in range (1,500):
    sohh=-1
    tong=0

    for j in range (1,i):
       
       if i%j==0:
           tong=tong+j
    if tong==i:
           sohh=i
           
    if i==sohh:
        print (i,end=",")

#-------------------------------------------
sum3=0
for n in range (1,201):
    songugiac=(n*(3*n-1))/2
    sum3=sum3+songugiac
print ("\n Tổng các số ngũ giác từ 1-200 là :",sum3)



       
