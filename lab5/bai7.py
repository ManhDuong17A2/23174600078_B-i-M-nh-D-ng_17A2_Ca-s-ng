chuoi=input('nhap chuoi :  ')
a=''
for i in range (00,128):
    a=a+str(i)+','
c=a.strip(',')
b=c.split(',')
chu=','
for i in b:
    kituchu=chr(int(i))
    chu=chu+str(kituchu)+','
chu=chu.strip(',')
bangkituchu=chu.split(',')

#===================================================================
#dem ki tu viet hoa
kituhoa=''
for i in range (65,91):
    for j in chuoi:
        if j==bangkituchu[i+1]:
            kituhoa=kituhoa+j
        
print ('co',len(kituhoa),'ki tu hoa gom:',kituhoa)
#===================================================================
#dem ki tu viet thuong
kituthuong=''
for i in range (97,123):
    for j in chuoi:
        if j==bangkituchu[i+1]:
            kituthuong=kituthuong+j
        
print ('co',len(kituthuong),'ki tu thuong gom:',kituthuong)
#===================================================================
#dem ki tu so
kituso=''
for i in range (48,58):
    for j in chuoi:
        if j==bangkituchu[i+1]:
            kituso=kituso+j
        
print ('co',len(kituso),'ki tu so gom:',kituso)
#===================================================================
#dem ki tu dac biet
kitudacbiet=''
for i in range (58,65):
    for j in chuoi:
        if j==bangkituchu[i+1]:
            kitudacbiet=kitudacbiet+j
        
for i in range (91,97):
    for j in chuoi:
        if j==bangkituchu[i+1]:
            kitudacbiet=kitudacbiet+j
for i in range (123,128):
    for j in chuoi:
        if j==bangkituchu[i+1]:
            kitudacbiet=kitudacbiet+j
for i in range (0,48):
    for j in chuoi:
        if j==bangkituchu[i+1]:
            kitudacbiet=kitudacbiet+j
print ('co',len(kitudacbiet),'ki tu dac biet gom:',kitudacbiet)
