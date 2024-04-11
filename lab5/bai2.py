a=input('nhap chuoi a: ')
b=input('nhap chuoi b: ')
chuoiconchungmin = ""
for i in range(len(b)):
    for j in range(len(b)):
      if a[i]==b[j]:
        chuoitamthoi = ""
        while i+len(chuoitamthoi)<len(a) and j +len(chuoitamthoi)<len(b) and a[i+len(chuoitamthoi)]==b[j+len(chuoitamthoi)]:
          chuoitamthoi += a[i + len(chuoitamthoi)]
        if len(chuoitamthoi) > len(chuoiconchungmin):
          chuoiconchungmin = chuoitamthoi
print (chuoiconchungmin)
