# 10진법 숫자를 2진법으로 표현하기
dec=int(input('Enter the decimal number you want to change to binary: '))

bi=''
q=dec

while True:
    if q==1 or q==0:
        bi+=str(q)
        break
    r=q%2
    bi+=str(r)
    q//=2

bi=list(bi)
bi.reverse()
bi=''.join(bi)
print('%d is a binary number of %s.'%(dec, bi))
