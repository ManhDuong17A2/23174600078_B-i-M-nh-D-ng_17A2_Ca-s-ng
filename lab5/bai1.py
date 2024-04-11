a=int(input('nhap so :  '))
sochia=a
nhiphan=''
while True :
     if sochia%2==0:
          nhiphan=nhiphan+'0'
          sochia=sochia/2
          if sochia==1:
               nhiphan=nhiphan+'1'
               break
     else :
          nhiphan=nhiphan+'1'
          sochia=(sochia-1)/2
          if sochia==1:
               nhiphan=nhiphan+'1'
               break
print (nhiphan[::-1])