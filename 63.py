#유클리드 호제법으로 최대공약수 구하기

def gcd(x,y):
    if y==0:
        return x
    if x%y==0:
        return y
    else:
        return gcd(y, x%y)
    
x=int(input('Please enter a value for x: '))
y=int(input('Please enter a value for y: '))

print('Greatest Common Divisor is', gcd(x,y))
