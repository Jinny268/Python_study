#제목 출력
print('## X, Y좌표의 사분면 위치 찾기##')

#값 입력 및 정수 변환
point_x=int(input('X축 좌표를 입력해주세요: '))
point_y=int(input('Y축 좌표를 입력해주세요: '))

#분기문
if point_x>0:

    if point_y>0:
        print('1사분면')
    elif point_y<0:
        print('4사분면')
    else:
        print('X축 위의 점이다.')

elif point_x<0:
    if point_y>0:
        print('2사분면')
    elif point_y<0:
        print('3사분면')
    else:
        print('X축 위의 점이다.')

else:

    if point_y==0:
        print('원점이다.')
    else:
        print('Y축 위의 점이다.')
