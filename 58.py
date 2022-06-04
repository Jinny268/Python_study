# 평균 구하기
a=[]

num=input('Please enter an number(enter an empty line to exit): ')
while num != '':
    a.append(num)
    num=input('Please enter an number(enter an empty line to exit): ')

a=[int(i) for i in a]

avg=sum(a)/len(a)
print('평균: ', avg)
print('리스트 값 들: ', int(a))
