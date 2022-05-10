month=input('Please enter the month by text: ')
day=int(input('Please enter the number of days: '))

if month=='January' or month=='February':
    print('Winter!')
elif month=='March':
    if day<20:
    	print('Winter!')
    elif day>=20:
    	print('Spring!')
elif month=='April' or month=='May':
    print('Spring!')
elif month=='June':
    if day<21:
    	print('Spring!')
    elif day>=21:
    	print('Summer!')
elif month=='July' or month=='August':
    print('Summer!')
elif month=='September':
    if day<22:
    	print('Summer!')
    elif day>=22:
    	print('Fall!')
elif month=='October' or month=='November':
    print('Fall!')
elif month=='December':
    if day<21:
    	print('Fall!')
    elif day>=21:
    	print('Winter!')
