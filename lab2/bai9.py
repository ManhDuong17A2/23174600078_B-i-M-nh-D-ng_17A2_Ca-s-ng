a1,b1=map(float,input('nhap he so goc và he so tu do:  ').split(','))
m,n,p=map (float,input('nhap toa do tam m,n ban kinh p:    ').split(','))
'''
y=a1x +b1 

'''
if a1==0:
   y=0
   x=m
   k=((m-x)**2+(n-y)**2)**0.5
if a1!=0:
 #A(x1,y1)
 x1=0
 y1=b1
 #B(x2,y2)
 y2=0
 x2=-b1/a1
 #AB
 xab=x2-x1
 yab=y2-y1
 #phaptuyen BC(xbc,ybc) vuong góc với AB 
 xbc=xab
 ybc=-yab
 #dt vuong goc vưới dt1 và di qua tam : xbc x + ybc y +c=0
 c=-xbc*m -ybc*n   

 '''
 xet tuong giao 2 dt y=a1x + b1 
               và  xbc x + ybc y + c =0                
 '''
 #có 
 x=(-c - ybc*b1)/(xbc+ybc) 
 y = a1*x +b1
 #khoảng cách tới tâm là 
 k=((m-x)**2+(n-y)**2)**0.5
if k==p:
     print ("dt tiep xuc dtron ")
if k>p:
     print ('dt nằm ngoài dtron ')
if k<p:
     print ('dt cắt dtron')