
for i in range (5):
    
    print (' '*(5-i-1),end='')
    for j in range (i+1):
        print ('* ',end='')
    print ()
for i in range (5): 
   

    print (' '*i,end="")
    for i in range(5-i):
        print ('*',end=' ')
    print ()
#----------------------------------------------
print ('==================================================')
for i in range (7):
    
    print (' '*(7-i-1),end='')
    for j in range (i,i+1):
        print ('*'*(2*j-1),end='')
    print ()
for i in range (3):
    print (' '*4+'*'*3)

print ()