# 연산자의 우선 순위 출력
def operator(pre):
    if pre=='+' or pre=='-':
        return 1
    elif pre=='*' or pre=='/':
        return 2
    elif pre=='^':
        return 3
    else:
        return -1

pre=str(input('Please enter mathematical operator: '))
print('The precedence of this operator is ', operator(pre))
