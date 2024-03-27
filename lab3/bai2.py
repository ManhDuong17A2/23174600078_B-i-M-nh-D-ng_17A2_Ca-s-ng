sum=0
for i in range (2000,4001):
    if i%7==0 and i%5!=0:
        sum = sum +i
print ('Tổng các số từ 2000-4000 chia hết cho 7 nhưng hông chia hết cho 5 là:' ,sum)

#------------------------------------------------------------------------------------
sum2=0
for i in range (500,1001):
    if i%4==0 and i%6!=0:
        sum2 =sum2+i
print ('Tổng các số từ 500-1000 chia hết cho 4 nhưng không chia hết cho 6 là: ',sum2)