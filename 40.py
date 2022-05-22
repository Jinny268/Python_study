# 가위바위보 게임
print('##가위, 바위, 보 게임##')

A=input('A를 위한 가위, 바위, 보를 입력하세요: ')
B=input('B를 위한 가위, 바위, 보를 입력하세요: ')

if A=='가위':
    if B=='가위':
        print('무승부')
    elif B=='바위':
        print('B 승리')
    elif B=='보':
        print('A 승리')
    else:
        print('B 값 입력 오류 ->', B)
        
elif A=='바위':
    if B=='가위':
        print('A 승리')
    elif B=='바위':
        print('무승부')
    elif B=='보':
        print('B 승리')
    else:
        print('B 값 입력 오류 ->', B)
        
elif A=='보':
    if B=='가위':
        print('B 승리')
    elif B=='바위':
        print('A 승리')
    elif B=='보':
        print('무승부')
    else:
        print('B 값 입력 오류 ->', B)

else:
    print('A 값 입력 오류 ->', A)
