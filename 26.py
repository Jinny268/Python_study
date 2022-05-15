# 휴대전화 요금제에 따른 한 달 사용 요금 구하기
m=int(input('Please enter the minutes: '))
t=int(input('Please enter the text: '))

p0=(15+0.44)*1.05
p1=(t-50)*0.15
p2=(m-50)*0.25

if m<=50:
    if t<=50:
        print('Base rate (including 911 fees and taxes): %.2f $.' %p0)
        print('Total Amount: %.2f $' %p0)
    elif t>50:
        print('Base rate (including 911 fees and taxes): %.2f $.' %p0)
        print('Additional Text Charges: %.2f $' %p1)
        print('Total Amount: %.2f $' %(p0+p1))

elif m>50:
    if t<=50:
        print('Base rate (including 911 fees and taxes): %.2f $.' %p0)
        print('Additional Minutes Charge: %.2f $' %p2)
        print('Total Amount: %.2f $' %(p0+p2))
    elif t>50:
        print('Base rate (including 911 fees and taxes): %.2f $.' %p0)
        print('Additional Minutes Charge: %.2f $' %p2)
        print('Additional Text Charges: %.2f $' %p1)
        print('Total Amount: %.2f $' %(p0+p1+p2))
