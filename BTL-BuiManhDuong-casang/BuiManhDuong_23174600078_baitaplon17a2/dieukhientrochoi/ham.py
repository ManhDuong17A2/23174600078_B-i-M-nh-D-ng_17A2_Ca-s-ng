import random 

import csv 

solanlac=0
ketqua=[]
ketquaxs={}
ketquanhieulanlac=[]



def lacsung():
  
   a = random.choice ([0,1])
   if a ==0 :
       print ('Click')
       ketqua.append('Click')
       return 'Click'
   else :
       print ('Bang')
       ketqua.append('Bang')
       return 'Bang'


def tinhxs (solanlac):
    for i in range(solanlac): 

     ketquaxs[i+1]=1/2 
    return ketquaxs 

  
    
def lacnhieulan(solanmuonlac,ketquanhieulanlac):
   
   for i in range (solanmuonlac):
       a = random.choice ([0,1])
       if a ==0 :
       
        ketquanhieulanlac.append('Click')
       
       else :
       
        ketquanhieulanlac.append('Bang')
    
   demBang=0
   demClick=0    
   for i in ketquanhieulanlac:
      if i == 'Bang':
         demBang=demBang+1
      else :
         demClick=demClick +1


   print ('so lan lac :',solanmuonlac,' , so lan trúng là : ', demBang,', số lần trượt là : ',demClick)






def saveincsv(duongdan):
                                    
    with open (duongdan,'w',newline='',encoding='utf-8') as file :
         viet=csv.writer(file )
         viet.writerows(ketqua)




def ketquacothexayra():
    kq={'Bang','Click'}
    print ('ket qua co the xay ra la : ',kq)



ketquaxsnhieulanlac=[]
def tinhxslacnhieulan(solanmuonlac):
   demBang=0
   demClick=0    
   for i in ketquanhieulanlac:
      if i == 'Bang':
         demBang=demBang+1
      else :
         demClick=demClick +1

   xsBang=tohopC(demBang,solanmuonlac)*(demBang**(1/2))*((solanmuonlac-demBang)**(1/2))
   xsClick=tohopC(demClick,solanmuonlac)*(demClick**(1/2))*((solanmuonlac-demClick)**(1/2))
   ketquaxsnhieulanlac.append(str(xsBang))
   ketquaxsnhieulanlac.append(str(xsClick))
   print ('xs trúng trong',solanmuonlac,'là :',xsBang)
   print ('xs truot trong',solanmuonlac,'là :',xsClick)



def savexsincsv(duongdan):
   with open(duongdan,'w',newline='',encoding='utf-8') as file :
      viet=csv.writer(file)
      viet.writerows(ketquaxsnhieulanlac)


   
   

def tohopC(k,n):
   ngiaithua=1
   for i in range (1,n+1):
      ngiaithua=ngiaithua*i
   n_kgiaithua=1
   for i in range (1,n-k+1):
      n_kgiaithua=n_kgiaithua*i
   kgiaithua=1
   for i in range (1,k+1):
      kgiaithua=kgiaithua*i
   tohopC=ngiaithua/(n_kgiaithua*kgiaithua)
   return tohopC


