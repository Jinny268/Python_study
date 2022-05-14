# 회사에서 직원을 평가한 등급 척도를 입력받아 금여 인상액 계산하기
a=float(input('Please enter your rating(0.0, 0.4 or more): '))

d=a*2400

if a==0.0:
    print('Unacceptable performance!')
    print('Your increase is %f $.' %d)
elif a==0.4:
    print('Acceptable performance!')
    print('Your increase is %f $.' %d)
elif a>=0.6:
    print('Meritorious performance!')
    print('Your increase is %f $.' %d)
else:
    print('This is an invalid input.')
