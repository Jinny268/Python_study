# 정수(양의 정수, 0, 음의정수)를 입력받아 오름차순으로 정리하기
nt=[]
z=[]
pt=[]

line=input('Please enter an integer (enter an empty line to exit): ')
while line != '':
    num=int(line)

    if num<0:
        nt.append(num)
    elif num>0:
        pt.append(num)
    elif num==0:
        z.append(num)

    line=input('Please enter an integer (enter an empty line to exit): ')

for n in nt:
    print(n)
for n in z:
    print(n)
for n in pt:
    print(n)
