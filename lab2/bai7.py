chieucao,cannang=map(float,input('nhap chieu cao,can nang:  ').split(','))
bmi=cannang/(chieucao**2)
if bmi<18.5:
    print ('gầy ')
if 18.5<=bmi<=24.9:
    print ('bình thường ')
if 25<=bmi<=29.9:
    print ('hơi béo ')
if bmi>=30:
    print ('béo ')
