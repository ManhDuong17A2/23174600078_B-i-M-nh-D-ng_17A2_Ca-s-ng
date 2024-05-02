danhsachthongtinsv=[]
stt=[i for i in range(1,11)]


for i in range (1,11):
    a=input(f'nhap ten  vien thu {i}:  ')
    b=float(input(f'nhap diem sinh vien {i}:  '  ))
    danhsachthongtinsv.append([a,b])
    
    
print ('danh sach thong tin sinh vien duoc nhap vao:  ')  
print (danhsachthongtinsv)

dict_thongtinvs={x:y for x,y in zip(stt,danhsachthongtinsv) }

print ('danh sach thong tin sinh vien sau khi da xep loai:  ')
print (dict_thongtinvs)
for i in dict_thongtinvs:
    if  dict_thongtinvs[i][1]<4:
        dict_thongtinvs[i].append('diem F')
    if  4<=dict_thongtinvs[i][1]<5.4:
        dict_thongtinvs[i].append('diem D')
    if  5.4<=dict_thongtinvs[i][1]<=6.9:
        dict_thongtinvs[i].append('diem C')
    if  7<=dict_thongtinvs[i][1]<=8.4:
        dict_thongtinvs[i].append('diem B')
    if  8.4<dict_thongtinvs[i][1]<=10:
        dict_thongtinvs[i].append('diem A')
danhsachsvdiemF=[]
danhsachsvdiemD=[]
danhsachsvdiemC=[]
danhsachsvdiemB=[]
danhsachsvdiemA=[]

print (dict_thongtinvs)
for i in dict_thongtinvs:
    if dict_thongtinvs[i][2]=="diem F":
        danhsachsvdiemF.append(dict_thongtinvs[i])
    if dict_thongtinvs[i][2]=="diem D":
        danhsachsvdiemD.append(dict_thongtinvs[i])
    if dict_thongtinvs[i][2]=="diem C":
        danhsachsvdiemC.append(dict_thongtinvs[i])
    if dict_thongtinvs[i][2]=="diem B":
        danhsachsvdiemB.append(dict_thongtinvs[i])
    if dict_thongtinvs[i][2]=="diem A":
        danhsachsvdiemA.append(dict_thongtinvs[i])
print ('so luong sinh vien diem F la :',len(danhsachsvdiemF))
print ('so luong sinh vien diem D la :',len(danhsachsvdiemD))
print ('so luong sinh vien diem C la :',len(danhsachsvdiemC))
print ('so luong sinh vien diem B la :',len(danhsachsvdiemB))
print ('so luong sinh vien diem A la :',len(danhsachsvdiemA))



