a='hello'
b='world'
c=''
for i in range (len(a)):
    c=c+a[i]+'-'+b[i]+'-'
print (c.strip('-'))