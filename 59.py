# 무작위로 복권 번호 생성하기
import random
lotto=random.sample(range(1,46),6)

lotto.sort()

print('*These are the six lottery numbers.*')
print('     ', lotto)
