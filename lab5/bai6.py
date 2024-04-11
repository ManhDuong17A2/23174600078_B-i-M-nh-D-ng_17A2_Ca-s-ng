chuoi=input('nhap chuoi :  ')
a=''
for i in range (00,48):
    a=a+str(i)+','

for i in range (58,65):
    a=a+str(i)+','
for i in range (91,97):
    a=a+str(i)+','
for i in range (123,128):
    a=a+str(i)+','
c=a.strip(',')
b=c.split(',')
chu=','
for i in b:
    kituchu=chr(int(i))
    chu=chu+str(kituchu)+','
chu=chu.strip(',')
chu=chu.lower()
bangkituchu=chu.split(',')

print ('cac ki tu dac biet trong chuoi la: ')
kitu=''
for i in chuoi:
    for j in bangkituchu:
        
      if i==j:
          kitu=kitu+i
          break
print(kitu)

#========================================================================================

for i in kitu:
    print ('so ki tu',i,'xuat hien trong chuoi',chuoi.count(i),'lan')

#========================================================================================

for i in kitu:
    k=chuoi.count(i)/int(len(chuoi))
    print ('ti le phan tram cua moi ki tu',i,'trong chuoi so voi tong ki tu trong chuoi la:',k)
            
