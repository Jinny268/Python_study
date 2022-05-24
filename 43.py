prices=[4.95, 9.95, 14.95, 19.95, 24.95]

print('original price - discount amount = new price for purchases')

for price in prices:
    print('%.2f $ - %.2f $ = %.2f $' %(price, price*0.6, price-(price*0.6)))
