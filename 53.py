# 1부터 12 중에서 입력 받은 수를 서수로 출력하기
def ordinal(a):
    if 1<=a<=12:
        ord={1: 'First', 2: 'Second', 3: 'Third', 4: 'Fourth', 5: 'Fifth', 6: 'Sixth', 7: 'Seventh', 8: 'Eighth', 9: 'Ninth', 10: 'Tenth', 11: 'Eleventh', 12: 'Twelfth'}
        return ord[a]
    else:
        return 0

a=int(input('Please enter a number(1~12): '))
print(ordinal(a))
        
