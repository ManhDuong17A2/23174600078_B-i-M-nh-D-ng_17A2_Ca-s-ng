a=[[1,2,3,4],
   [4,5]]
lenmax=0
for i in a:
    if len(i)>lenmax:
        lenmax=len(i)
if len(a)<lenmax:
    for i in range(lenmax-len(a)):
        a.append([])
for i in a :
    if len(i)<lenmax:
        for j in range (lenmax-len(i)):
            i.append(0)
print (a)
tongds=[]
tong=0
for i in range (len(a)):
    for j in range((len(a[1]))):
        tong=tong+a[j][i]
    tongds.append(tong)
    tong=0
print (tongds)
