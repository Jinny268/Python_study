# for문을 사용하여 홀수의 합에서 최초로 100이 넘는 위치 구하기
hap, i=0, 0

for i in range(1, 102, 2):
    hap+=i

    if hap>=1000:
        break

print('1~100의 홀수의 합에서 최초로 100이 넘는 위치: %d' %i)
