import random
lotto=random.sample(range(1,46),6)

lotto.sort()

print('*These are the six lottery numbers.*')
print('     ', lotto)
