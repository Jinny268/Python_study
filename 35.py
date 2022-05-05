year=int(input('How old is a dog in human year? '))

if 0<year<=2:
    year=year*10.5
    print('dog year is ', year)
elif year>2:
    year=(10.5*2)+(year-2)*4
    print('dog year is ', year)
elif year<=0:
    print('Invalid input.')
