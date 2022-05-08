len1=int(input('첫 번째 변의 길이를 입력하세요: '))
len2=int(input('두 번째 변의 길이를 입력하세요: '))
len3=int(input('세 번째 변의 길이를 입력하세요: '))

if len1==len2==len3:
	print('정삼각형입니다.')
elif len1==len2 or len1==len3 or len2==len3:
	print('이등변 삼각형입니다.')
else:
	print('부등변 삼각형입니다.')
