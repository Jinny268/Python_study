# 행과 열에 맞추어 1~10까지의 곱 출력하기
print('    ', end='')

for i in range(1, 11):
    print('%4d' %i, end='')
print()

for i in range(1, 11):
    print('%4d' %i, end='')
    for j in range(1, 11):
        print('%4d' %(i*j), end='')
    print()
