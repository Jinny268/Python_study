'''
# 값 입력
flag = input('마음에 드는 옷을 찾았나요?(예/아니요): ')

# 조건 분기
if flag == '예':
    print(':) 축하합니다!!')
elif flag == '아니요':
    print(':( 아쉽군요.')
else:
    print('ㅜㅜ잘못된 입력입니다.')
'''

# 값 입력
flag=input('마음에 드는 옷을 찾았나요? (예/아니요): ')

# 조건 분기
if flag=='예':
    print('축하드려요!!')

    price=input('가격이 얼마인가요?')

    if int(price) <= 50000:
        print('구매합시다!')
    else:
        print('포기합니다ㅜ')
elif flag=='아니요':
    print('아쉽군요ㅜㅜ')
else:
    print("'예' 또는 '아니요'로만 입력해주세요!")
