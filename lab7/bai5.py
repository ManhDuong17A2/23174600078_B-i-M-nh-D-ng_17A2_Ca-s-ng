kho={'banana':6,
     'apple':5,
     'orange':32,
     'pear':15}
gia_tien={'banana':4,
          'apple':2,
          'orange':1.5,
          'pear':3}
thongtinmuahang={}
dongia={}
while True : 
 a=input('nhap mat hang da mua : ')
 b=int(input('nhap so luong mat hangf da mua:  '))
 thongtinmuahang[a]=b
 if a in gia_tien:
  dongia[a]=gia_tien[a]
 c=int(input('con thong tin nhap 1 , het thong tin nhap 0: '))
 if c==0:
  break
print ('thong tin mua hang la (mat hang , so luong ): ',thongtinmuahang)
print ('don gia cua mat hang da mua la :',dongia)
tonghoadon=0
for i in thongtinmuahang:
 sotien=thongtinmuahang[i]*dongia[i]
 tonghoadon=tonghoadon+sotien
 print( f'so tien mua {i} la : ',sotien)
print ('tong hoa don la: ' , tonghoadon)

for i in thongtinmuahang:
    if i in kho :
        kho[i]=kho[i]-thongtinmuahang[i]
print (kho)

