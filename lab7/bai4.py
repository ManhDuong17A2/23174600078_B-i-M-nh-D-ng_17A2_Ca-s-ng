inventory={'gold':500,
           'pouch':['flint','twine','gemstone'],
           'backpack':['xylophone','dagger','bedroll','bread loaf']}

#them key
inventory['pocket']=['seashell','strange','lint']
# sap xep cac phan tu trong 'bachpack' key , em chua hieu la sap xep theo dinh dang nao, chữ cái đầu abc hay độ dài .... không biết đề có ghi thiếu k ạ ? 
#loại bỏ biến dagger     
inventory['backpack'].remove('dagger')
#them gt 50 vao gold key 
inventory['gold']=[500,50]
print (inventory)