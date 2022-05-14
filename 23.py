a=float(input('Please enter your rating(0.0, 0.4 or more): '))

d=a*2400

if a==0.0:
    print('Unacceptable performance!')
    print('Your increase is %f $.' %d)
elif a==0.4:
    print('Acceptable performance!')
    print('Your increase is %f $.' %d)
elif a>=0.6:
    print('Meritorious performance!')
    print('Your increase is %f $.' %d)
else:
    print('This is an invalid input.')
