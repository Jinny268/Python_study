month=int(input('당신이 태어난 달을 입력해주세요(숫자만 입력): '))
day=int(input('당신이 태어난 일을 입력해주세요(숫자만 입력): '))

if month==12:
	if 22<=day<=31:
		print('생일이 %d월 %d일인 당신은 Capricorn 자리입니다.' %month %day)
	elif 1<=day<=21:
		print('생일이 %d월 %d일인 당신은 Sagittarius 자리입니다.' %month %day)
elif month==1:
	if 1<=day<=19:
		print('생일이 %d월 %d일인 당신은 Capricorn 자리입니다.' %month %day)
	elif 20<=day<=31:
		print('생일이 %d월 %d일인 당신은 Aquarius 자리입니다.' %(month, day))
elif month==2:
	if 1<=day<=18:
		print('생일이 %d월 %d일인 당신은 Aquarius 자리입니다.' %(month, day))
	elif 19<=day<=29:
		print('생일이 %d월 %d일인 당신은 Pisces 자리입니다.' %(month, day))
elif month==3:
	if 1<=day<20:
		print('생일이 %d월 %d일인 당신은 Pisces 자리입니다.' %(month, day))
	elif 21<=day<=31:
		print('생일이 %d월 %d일인 당신은 Aries 자리입니다.' %(month, day))
elif month==4:
	if 1<=day<=19:
		print('생일이 %d월 %d일인 당신은 Aries 자리입니다.' %(month, day))
	elif 20<=day<=30:
		print('생일이 %d월 %d일인 당신은 Taurus 자리입니다.' %(month, day))
elif month==5:
	if 1<=day<=20:
		print('생일이 %d월 %d일인 당신은 Taurus 자리입니다.' %(month, day))
	elif 21<=day<=31:
		print('생일이 %d월 %d일인 당신은 Gemini 자리입니다.' %(month, day))
elif month==6:
	if 1<=day<=20:
		print('생일이 %d월 %d일인 당신은 Gemini 자리입니다.' %(month, day))
	elif 21<=day<=30:
		print('생일이 %d월 %d일인 당신은 Cancer 자리입니다.' %(month, day))
elif month==7:
	if 1<=day<=22:
		print('생일이 %d월 %d일인 당신은 Cancer 자리입니다.' %(month, day))
	elif 23<=day<=31:
		print('생일이 %d월 %d일인 당신은 Leo 자리입니다.' %(month, day))
elif month==8:
	if 1<=day<=22:
		print('생일이 %d월 %d일인 당신은 Leo 자리입니다.' %(month, day))
	elif 23<=day<=31:
		print('생일이 %d월 %d일인 당신은 Virgo 자리입니다.' %(month, day))
elif month==9:
	if 1<=day<=22:
		print('생일이 %d월 %d일인 당신은 Virgo 자리입니다.' %(month, day))
	elif 23<=day<=30:
		print('생일이 %d월 %d일인 당신은 Libra 자리입니다.' %(month, day))
elif month==10:
	if 1<=day<=22:
		print('생일이 %d월 %d일인 당신은 Libra 자리입니다.' %(month, day))
	elif 23<=day<=31:
		print('생일이 %d월 %d일인 당신은 Scorpio 자리입니다.' %(month, day))
elif month==11:
	if 1<=day<=21:
		print('생일이 %d월 %d일인 당신은 Scorpio 자리입니다.' %(month, day))
	elif 22<=day<=30:
		print('생일이 %d월 %d일인 당신은 Sagittarius 자리입니다.' %(month, day))
else:
	print('잘못된 입력입니다.')
	
