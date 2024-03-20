a=int(input("nhap vao so nguyen co 3 chu so: "))
sohangtram=a//100 
sohangchuc=(a-((a//100)*100))//10
sohangdv=a-(a//100)*100-(((a-((a//100)*100))//10)*10)
hundred_and='hundred and'

if sohangtram==1:
    m='A'
if sohangtram==2:
    m='Two'
if sohangtram==3:
    m='Thrre'
if sohangtram==4:
    m='four'
if sohangtram==5:
    m='five'
if sohangtram==6:
    m='six'
if sohangtram==7:
    m='seven'
if sohangtram==8:
    m='eight'
if sohangtram==9:
    m='nine'
if sohangchuc==0:
    n=''
if sohangchuc==2:
    n='twenty'
if sohangchuc==3:
    n='thirt'
if sohangchuc==4:
    n='forty'
if sohangchuc==5:
    n='fifty'
if sohangchuc==6:
    n='sixty'
if sohangchuc==7:
    n='seventy'
if sohangchuc==8:
    n='eighty'
if sohangchuc==9:
    n='ninety'
if sohangdv==1:
    p='one'
if sohangdv==2:
    p='two'
if sohangdv==3:
    p='three'
if sohangdv==4:
    p='for'
if sohangdv==5:
    p='five'
if sohangdv==6:
    p='six'
if sohangdv==7:
    p='seven'
if sohangdv==8:
    p='eight'
if sohangdv==9:
    p='nine'
if sohangchuc==1:
    n=''
    if sohangdv==0:
       p='ten'
    if sohangdv==1:
       p='eleven'
    if sohangdv==2:
       p='twelve'
    if sohangdv==3:
       p='thirteen'
    if sohangdv==4:
       p='fourteen'
    if sohangdv==5:
       p='fifteen'
    if sohangdv==6:
       p='sixteen'
    if sohangdv==7:
       p='seventeen'
    if sohangdv==8:
       p='eighteen'
    if sohangdv==9:
       p='nineteen'
read=m+' '+hundred_and+' '+n+' '+p
print (read)