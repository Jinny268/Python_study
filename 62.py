# 재귀를 이용하여 합계 구하기
def plus():
    num=input('Please enter a number (enter an empty line to exit): ')

    if num=='':
        return 0
    else:
        return float(num) + plus()

def main():
    total=plus()
    
    print('The total is',total)

main()
