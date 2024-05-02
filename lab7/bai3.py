'''Mahatama Gandhi is our national father.
 He is the apostle of truth, honesty and nonviolence.
   He transformed himself from a common man to a great man by dedicating his life for a great cause.
He prepared people to fight for freedom without violence.
 His method was unique. He believed in the goodness of human heart.
   Even oppressor’s heart can be converted with love and sincerity.
     He brought freedom to us. His ideas, methods and dedication attracted the world attention. 
     His fight was against inhumanity. In all his moments and decisions he put common man at the centre. 
He is rightly called ‘Mahatama’ by the people. '''
a="Mahatama Gandhi is our national father. He is the apostle of truth, honesty and nonviolence. He transformed himself from a common man to a great man by dedicating his life for a great cause."
b="He prepared people to fight for freedom without violence. His method was unique. He believed in the goodness of human heart. Even oppressor’s heart can be converted with love and sincerity. He brought freedom to us. His ideas, methods and dedication attracted the world attention. His fight was against inhumanity. In all his moments and decisions he put common man at the centre. He is rightly called ‘Mahatama’ by the people. "
c=a+b

d=c.split(',' and '.' and ' ' )
e=[]

for i in d:
   k=i.lower()
   h=k.rstrip('.')
   e.append(h)

stt=[i for i in range (len(e))]
dict_danhsachtu={x:y for x,y in zip(e,e)}
print(dict_danhsachtu)
danhsachtutrungnhau={}
for i in dict_danhsachtu:
   dem=0
   for j in e :
      if dict_danhsachtu[i]==j:
         dem=dem+1
   danhsachtutrungnhau[i]=dem

#sẽ tạo ra một từ điển bao gồm khóa là một từ và value là số lần xuất hiện của từ đó trong đoạn văn trên

print (danhsachtutrungnhau)
max = 0
for i in danhsachtutrungnhau:
   if danhsachtutrungnhau[i] >max:
      max=danhsachtutrungnhau[i]
dsmax=[]
for i in danhsachtutrungnhau:
   if danhsachtutrungnhau[i]==max :
      dsmax.append(i)
print ('danhsach cac tu trung nhau nhieu nhat la: ', dsmax,'có',max,'lần xuất hiện  ')
dsmin=[]
min=max
for i in danhsachtutrungnhau:
   if danhsachtutrungnhau[i]<min:
      min=danhsachtutrungnhau[i]
for i in danhsachtutrungnhau:
   if danhsachtutrungnhau[i]==min:
      dsmin.append(i)
      
print ('danh sach cac tu trung nhau it nhat la: ',dsmin, 'cac tu này có ',min,' lần xuất hiện  ')


      
