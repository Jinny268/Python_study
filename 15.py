# 체스판에서 해당 위치의 색 알아보기
wid=input('가로 값이 될 알파벳을 입력해주세요(a~h): ')
ver=int(input('세로 값이 될 숫자를 입력해주세요(1~8): '))

if wid=='a' or wid=='c' or wid=='e' or wid=='g':
	if ver==1 or ver==3 or ver==5 or ver==7:
	    print('Black!')
	elif ver==2 or ver==4 or ver==6 or ver==8:
	    print('White!')
elif wid=='b' or wid=='d' or wid=='f' or wid=='h':
	if ver==1 or ver==3 or ver==5 or ver==7:
	    print('White!')
	elif ver==2 or ver==4 or ver==6 or ver==8:
	    print('Black!')
