#permutations (P)
def P(n,r):
   tuso=1
   for i in range (1,n+1):
      tuso=tuso*i
   mauso=1
   for i in range (1,n-r+1):
      mauso=mauso*i
   p=tuso/mauso
   return p
def C(n,r):
   tuso=1
   for i in range (1,n+1):
      tuso=tuso*i   
   mauso=1
   for i in range (1,n-r+1):
      mauso=mauso*i
   mauso2=1
   for i in range (1,r+1):
      mauso2=mauso2*i
   c=tuso/(mauso2*mauso)
   return c
print (P(3,2))
print (C(3,2))