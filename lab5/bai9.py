b=input('nhap chuoi ban dau: ')
a=input('nhap chuoi 2: ')
h= (a[len(b)::])
if len (a)>len(b) and a[0:len(b)]==b:
    b=b+a[len(b)::]
    
    
    print ('sau khi them cac ki tu',h ,'ta duoc chuoi ban dau thanh chuoi 2:',b)
else :
    print ('khong the dung cach them ki tu de bien chuoi ban dau thanh chuoi 2')
#==========================================================================================
if len(b)==len(a):
    for i in range(len(b)):
        if b[i]!=a[i]:
            
            print ('thay the ki tu:',b[i],'chuoi ban dau thanh ki tu',a[i]) 
    print ('ta duoc chuoi ban dau thanh chuoi 2:',a)
else:
    print ('khong the dung cach thay the de bien chuoi ban dau thanh chuoi 2')
    