#tạo dãy fibonacci bằng list comprehension
fibonacci_list=[0,1]
n=int(input('nhap n: '))
[fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2]) for i in range(2, n)]
print ('dãy fibonacci la : ',fibonacci_list )


#tạo dãy số nguyên tố bằng list comprehension 
snt_list=[]
n=int(input('nhap n : '))
[snt_list.append(j) for j in range (n) if all(j % i != 0 for i in range(2, int(j**0.5) + 1)) and j!=0]
print('day fibonacci la : ', snt_list)

