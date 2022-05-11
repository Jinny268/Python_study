# 생일을 입력하여 띠 알아보기
year=int(input('Please enter only the number of years: '))

if year>0:
    if year%12==0:
        print('The animal of this year is a Monkey.')
    elif year%12==1:
        print('The animal of this year is a Rooster.')
    elif year%12==2:
        print('The animal of this year is a Dog.')
    elif year%12==3:
        print('The animal of this year is a Pig.')
    elif year%12==4:
        print('The animal of this year is a Rat.')
    elif year%12==5:
        print('The animal of this year is a Ox.')
    elif year%12==6:
        print('The animal of this year is a Tiger.')
    elif year%12==7:
        print('The animal of this year is a Hare.')
    elif year%12==8:
        print('The animal of this year is a dragon.')
    elif year%12==9:
        print('The animal of this year is a Snake.')
    elif year%12==10:
        print('The animal of this year is a Horse.')
    elif year%12==11:
        print('The animal of this year is a Sheep.')
elif year<=0:
    print('This is an invalid input.')
