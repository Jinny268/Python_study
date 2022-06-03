# 정확한 자료조사를 위해 극단적인 값 제거하기
def rem(data, num_1):
    retval=sorted(data)

    for i in range(num_1):
        retval.pop()
        
    for i in range(num_1):
        retval.pop(0)

    return retval

def main():
    cards = []
    c=input('Please enter a value (enter an empty line to exit): ')
    
    while c != '':
        num=float(c)
        cards.append(num)
        c=input('Please enter a value (enter an empty line to exit): ')

    if len(cards)<4:
        print('Please enter at least 4 values.')
    else:
        print('List from which outliers have been removed: ', rem(cards, 2))
        print('The original data: ', cards)

main()
