a=int (input('nhap n: '))
b=[int(input('nhap phan tu : ')) for i in range (a)]
print (b)
index=0
congsai=b[1]-b[0]
csc=True 
while True:
   if index < int(len(b)):
    
    if b[index+1]-b[index]!=congsai   :
        print('day nay khong phai cap so cong ')
        csc=False 
        break 
   if index==int(len(b)-2):
      break
   index=index+1
if csc == True :
    print('day la cap so cong')



