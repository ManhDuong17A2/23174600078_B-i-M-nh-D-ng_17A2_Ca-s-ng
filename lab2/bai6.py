a,b,c=map(int,input('nhap 3 so nguyen:  ').split(','))
if a<b<c or c<b<a:
    print('so lon thu 2 là:',b)
if a<c<b or b<c<a:
    print ('so lon thu 2 la:',c)
if c<a<b or b<a<c:
    print ('so lon thu 2 la:',a)
    