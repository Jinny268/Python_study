import math

a=int(input('ax^2+bx+c에서 a의 값을 입력하세요(0이 될 수 없습니다.): '))
b=int(input('ax^2+bx+c에서 b의 값을 입력하세요: '))
c=int(input('ax^2+bx+c에서 c의 값을 입력하세요: '))

d=b**2-4*a*c

if d>0:
    root1=(-b+(b**2-4*a*c)**0.5)/2*a
    root2=(-b-(b**2-4*a*c)**0.5)/2*a
    print('이 방정식은 %f와 %f의 두 근을 가지고 있습니다.' %(root1, root2))
elif d==0:
    root3=-b/2*a
    print('이 방정식은 %f의 하나의 근을 가지고 있습니다.' %root3)
else:
    print('이 방정식은 어떠한 근도 가지고 있지 않습니다.')
