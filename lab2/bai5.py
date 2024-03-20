a=int(input('nhap so nguoi xem :  '))
if a==1 :
    giave=120000
if 2<=a<=4:
    giave=120000*a - (120000*a*(5/100))
if 4<=a<=10:
    giave=120000*a - (120000*a*(10/100))
if a>10:
    giave=120000*a - (120000*a*(20/100))
print('so tien phai trả cho',a,'nguoi xem la:',giave)