flag=input('Please enter 8 bits: ')

while flag !='':
    if flag.count('0')+flag.count('1')!=8 or len(flag)!=8:
        print('This is not 8 bits.')
    else:
        ones=flag.count('1')
        if ones%2==0:
            print('Parity bit must be 0.')
        elif ones%2==1:
            print('Parity bit must be 1.')
    break
