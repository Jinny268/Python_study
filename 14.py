# 달 별 휴일 여부 알려주기
month=int(input('월을 입력하세요(숫자로 입력해주세요.): '))
day=int(input('일을 입력하세요: '))

if month==1 and day==1:
	print("New year's day")
elif month==7 and day==1:
	 print('Canada day')
elif month==12 and day==25:
	print('Christmas day')
else:
	print('정해진 날에 휴일이 없습니다.')
