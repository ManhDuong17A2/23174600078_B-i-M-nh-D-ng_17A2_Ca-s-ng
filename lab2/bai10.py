phim=input('nhập phim bạn muốn xem (Hành động,Kinh dị,Tình cảm ,Hài hước ,Hoạt hình :  )')
tg=input("nhập thời gian muốn xem phim (sáng, trưa , chiều,tối ):  ")
if phim == 'Hành động' or phim =='Hài hước':
    print ('phim',phim,'thời gian xem',tg)
if phim == 'Kinh dị':
    if tg=='tối':
        print ('phim',phim,'thơi gian xem',tg)
    else:
        print ('khong co suất chiếu ')
if phim =='Tình cảm':
    if tg=='tối':
        print ('phim',phim,'thơi gian xem',tg)
    else :
        print ('khong có suất chiếu ')
if phim == 'Hoạt hình':
    if tg=='sáng' or tg=='trưa':
        print ('phim',phim,'thơi gian xem',tg)
    else:
        print ('không có suất chiếu ')