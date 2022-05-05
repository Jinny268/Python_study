# 개의 나이 사람의 나이로 환산
year=int(input('How old is a dog in human year? '))

# 개의 나이에 따라 환산법이 달라짐
if 0<year<=2:
    year=year*10.5
    print('dog year is ', year)
elif year>2:
    year=(10.5*2)+(year-2)*4
    print('dog year is ', year)
elif year<=0:
    print('Invalid input.')
