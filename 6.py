# 홀수, 짝수 판별
num=int(input('Please enter a number: '))

if num==0:  # 0은 홀수 짝수 둘 다 아님
    print('It is neither odd nor even.')
elif num%2==1:   # 2로 나누었을 때 나머지가 1이면 홀수
    print('Odd number!')
elif num%2==0:   # 2로 나누었을 때 나머지가 0이면 짝수
    print('Even number!')
