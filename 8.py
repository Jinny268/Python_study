answer=input('알파벳을 입력하세요: ')

if answer=='a' or answer=='e' or answer=='i' or answer=='o' or answer=='u':
	print('%c는 모음입니다.' %answer)
elif answer=='y':
	print('%c는 모음 또는 자음이 될 수 있습니다.' %answer)
else:
	print('%c는 자음입니다.' %answer)
