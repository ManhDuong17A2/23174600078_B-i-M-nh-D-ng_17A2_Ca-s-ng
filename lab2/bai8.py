'''
y=a1x+b1
y=a2x+b2
'''
a1,b1=map(float,input('nhap he so goc,he so tu do cua dt 1: ').split(','))
a2,b2=map(float,input('nhap he so goc va he so tu do của dt 2: ').split(','))
if a1==a2 and b1!=b2: 

    print ('day la hai dt song song ')
if a1!=a2 :
 if a1==0 or a2==0:
    print ("day la hai dt cheo nhau")



 if a1!=0 and a2!=0:
#A(x1,y1) in dt1 
    x1=0 
    y1=b1
#B(x2,y2) in dt1 
    y2=0
    x2=-b1/a1 
#C(x3,y3) in dt2 
    x3=0
    y3=b2 
#D(x4,y4) in dt2 
    y4=0
    x4=-b2/a2  
    tichvohuong=(x2-x1)*(x4-x3)+(y2-y1)*(y4-y3)
    if tichvohuong==0:
        print ('hai duong thang nay vuong goc ')
    else :
       print ('hai duong thang nay cheo nhau ') 