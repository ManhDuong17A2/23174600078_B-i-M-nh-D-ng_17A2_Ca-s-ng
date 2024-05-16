def sole(a):
    if a!=0:
     if a%2!=0:
        return True 
     else :
        return False 
     
      
def sochan(a):
    if a!=0:
     if a%2==0:
        return True 
     else :
        return False 
    
#-------------------------------------------------------
#dùng hàm filter để lọc 

def locle(danhsach):
 danhsachloc=filter(sole, danhsach)
 for i in danhsachloc:
  print(i)
print (locle([1,2,5,3,2,2,2,3,4,56,68,7]))
#-------------------------------------------------------
def locchan(danhsach):
 danhsachloc=filter(sochan, danhsach)
 for i in danhsachloc:
  print(i)


print (locchan([4,2,3,5,8,9,0,5]))
#--------------------------------------------------------
#dùng hàm map 
def sudungmap(ds):
  a=map(  lambda x : x**3  , ds)
  return list(a)
print (sudungmap([1,2,3]))
#----------------------------------------------------------
#dùng hàm map+filter tính lập phương số chẵn 
def locchan2(danhsach):
 danhsachloc=filter(sochan, danhsach)
 ds=[]
 for i in danhsachloc:
   ds.append(i)
 return ds 


def sudungmap(ds):
  a=map(  lambda x : x**3  , ds)
  return list(a)
  
print (sudungmap(locchan2([1,2,3,4,5,6])))
#-----------------------------------------------------------
#dùng map và filter để tính bình phương số lẻ 
def locle2(danhsach):
 danhsachloc=filter(sole, danhsach)
 ds=[]
 for i in danhsachloc:
   ds.append(i)
 return ds 
def sudungmap(ds):
  a=map(  lambda x : x**2 , ds)
  return list(a)
  
print (sudungmap(locle2([1,2,3,4,5,6])))


