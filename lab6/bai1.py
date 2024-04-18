a=int(input('nhap n:'))
b=[int(input('nhap:') )for i in range(a)]
tongchan=0
tongle=0
daychan=[]
dayle=[]
for i in b:
    if i%2==0:
        tongchan=tongchan+i
        daychan.append(i)
    if i%2!=0:
        tongle=tongle+i 
        dayle.append(i)
print ('day chan la:',daychan,'tong chan la:',tongchan)
print ('day le la:',dayle,'tong le la: ',tongle )