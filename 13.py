# 지폐 별 위인 알아보기
money=int(input('궁금하신 지폐의 금액을 입력하세요(단위는 달러이며, 숫자만 입력해주세요.): '))

if money==1:
	print('George Washington')
elif money==2:
	print('Thomas Jefferson')
elif money==5:
	print('Aberham Lincoln')
elif money==10:
	print('Alexander Hamilton')
elif money==20:
	print('Andrew Jackson')
elif money==50:
	print('Ulysses S.Grant')
elif money==100:
	print('Benjamin Fanklin')
else:
	print('잘못된 입력 또는 정해진 위인이 없습니다.')
