total=0
while True:
    p=input('Price: ')
    if p=='':
        break
    total = total+int(p)
    np=total*(100%5)

if np<(5/2):
    cash=total-(np/100)
else:
    cash=total+0.05-(np/100)
print('Cash: ', cash)
