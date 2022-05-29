# 암호 해결하기
m=input('Please enter a message: ')
s=int(input('Please enter the shift value: '))

n_m=''
for ch in m:
    if ch>='a' and ch<='z':
        p=ord(ch)-ord('a')
        p=(p+s)%26
        n_c=chr(p+ord('a'))
        n_m=n_m+n_c
    elif ch>='A' and ch <='Z':
        p=ord(ch)-ord('A')
        n_c=chr(p+ord('A'))
        n_m=n_m+n_c
    else:
        n_m=n_m+ch

print("This shifted message is '%s'." %n_m)
