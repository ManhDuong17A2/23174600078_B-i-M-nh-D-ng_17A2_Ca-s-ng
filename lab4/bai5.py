while True :
    a,b=map(int,input("nhap hai so a,b :   ").split(','))
    tong=a+b
    hieuab=a-b
    hieuba=b-a
    tich=a*b
    thuongab=a/b
    thuongba=b/a
    luythuaab=a**b
    luythuaba=b**a
    cana=a**(1/2)
    canb=b**(1/2)
    print ("Tổng hai số là: ",tong)
    print ('Hiệu a-b là: ',hieuab)
    print ('Hiệu b-a là: ',hieuba)
    print ('Tích hai số là: ',tich)
    print('a chia b bằng: ',thuongab)
    print ('b chia a bằng; ',thuongba)
    print ('lũy thừa bậc a của b bằng : ', luythuaba)
    print ('lũy thừa bậc b của a bằng : ', luythuaab)

    select=input('Nếu không muốn nhập tiếp xin vui lòng điền "không" :  ')
    if select=="không":
        break 

