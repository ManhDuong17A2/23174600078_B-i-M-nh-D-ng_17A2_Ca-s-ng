def snt(a):
    if a!=0:
     for i in range (2,a): 
        if a%i==0:
            return False         
     return True 

def sole(a):
   if a%2!=0:
      return True 
   else :
      return False 
k=[]
for i in range (1000):
    if sole(i):
       k.append(i)
run=0
for i in k :
   if snt(k[run]) and snt (k[run+1]):
      print ('cap snt sinh doi la : ', k[run],',',k[run+1])
   if k[run+1]==k[-1]:
     break
   run=run+1
