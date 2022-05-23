# 마음에 드는 옷을 찾을 때까지 반복하는 프로그램
# 반복문 수행 유무 플래그
repeat=True

# repeat이 True인 경우 whlie문 블록 수행
while repeat:

    # 값 입력
    flag = input('마음에 드는 옷을 찾았나요? (예/아니요): ')

    # 조건 분기
    if flag == '예':
        print(":) 축하합니다!!")
        repeat = False   # repeat가 False가 되었으므로 반복 종료

    else:
        print(':( 아쉽군요')
        print('다른 매장에서 골라보세요!')
