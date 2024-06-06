import csv 
import ham
from ham import *
import os 
duongdannoi=os.getcwd()
noipath='\\ketqua.csv'
duongdan=duongdannoi+noipath

while True :
    print ('Tro choi lac sung : ')
    print ('1.lac sung ')
    print ('2.In ra ket qua cac lan lac sung ')
    print ('3.Tinh xac suat cua moi lan lac sung ')
    print ('4.Luu ket qua cac lan lac sung vao csv ')
    print ('5.Lac nhieu lan và In ket qua cua cac lan lac sung khi đã nhập số lần muốn lắc  ')
    print ('6.Tinh xs của cac lan lac sung ')
    print ('7.Luu ket qua tinh xs cua nhieu lan lac vào csv ')
    print ('8.Thoat')

    select = int (input("nhap lua chon cua ban 1,2,3,4,5:  "))
    if select ==1:
       ham.ketquacothexayra()
       ham.lacsung()
       solanlac=solanlac+1
    if select ==2:
        print (ketqua)
    if select ==3:
        ham.tinhxs(solanlac)
        print(ketquaxs)
    if select ==4:
        ham.saveincsv(duongdan)
         
    if select ==5:
        solanmuonlac=int(input('nhap so lan muon lac :  '))
        ham.lacnhieulan(solanmuonlac,ketquanhieulanlac)

    if select ==6:
        ham.tinhxslacnhieulan(solanmuonlac)

    if select==7:
        ham.savexsincsv(duongdan)
        print (ketquaxsnhieulanlac)
    if select==8:
        break 


       



          
      