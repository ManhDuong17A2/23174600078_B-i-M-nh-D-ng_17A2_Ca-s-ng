print ('Các số nguyên tố nhỏ hơn 1000 là :')
a=1
sknt=-1
while a<100:
    a=a+1 
    b=1
    while b<a-1:
        b=b+1
        if a%b==0:
            sknt=a
                
    if a!=sknt:
        print (a,end=',')

print ('\n Các số chính phương nhỏ hơn 100 là :')

a=1
scp=-1
while a<100:
    a=a+1 
    b=1
    while b<a-1:
        b=b+1
        if b**2==a:
            scp=a
                
    if a==scp:
        print (a,end=',')

print ("\n Dãy số fibonanci có số cuối nhỏ hơn 1000 là :")
a,b=0,1
print (a,b)
while True :
    
    c=a+b
    a=b
    b=c
    if c>=1000:
        break 
    print (c,end=',')
    
