import re

p=input('Please enter your license plate: ')

result=re.match('[A-Z]+[0-9]{3}', p)
length=len(result.group())

if length==6:
    print('Older style plate!')
elif length==7:
    print('Newer style plate!')
else:
    print('This is an invalid input.')
