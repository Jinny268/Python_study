# 윤년 판별하기
year=int(input('년도를 입력하세요(숫자만 입력): '))

if year%400==0:
    print('%d년은 윤년입니다.' %year)
else:
    if year%4==0:
        if year%100==0:
            print('%d년은 윤년이 아닙니다.' %year)
        else:
            print('%d년은 윤년입니다.' %year)
    else:
        print('%d년은 윤년이 아닙니다.' %year)
