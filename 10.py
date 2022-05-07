# 달 별 일수 알아보기
month=int(input('일 수가 궁금한 월을 입력하세요(숫자만 입력해주세요): '))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
	print('%d월의 일 수는 31일입니다.' %month)
elif month==4 or month==6  or month==9 or month==11:
	print('%d월의 일 수는 30일입니다.' %month)
elif month==2:
	print('%d월의 일 수는 28일 또는 29일입니다.' %month)
