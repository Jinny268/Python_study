# 랜덤값으로 주사위 숫자를 받아 대소 비교하기
import random

num_a=random.randrange(1,7)
print("A의 주사위 숫자는 %d 입니다." %num_a)

num_b=random.randrange(1,7)
print("B의 주사위 숫자는 %d 입니다." %num_b)

if num_a>num_b:
    print('A가 이겼다.')
elif num_a<num_b:
    print('B가 이겼다.')
else:
    print('둘이 비겼네요.')
