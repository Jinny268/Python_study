i=int(input('Please enter an integer: '))

if i<2:
    print('Invalid input.')
else:
    for divisor in range(2, i+1):
        count=0
        while i%divisor==0:
            i//=divisor
            count+=1
        if count>0:
            print("{}^{}".format(divisor,count), end=' ')
            if i>1:
                print("X", end=' ')
            else:
                break
