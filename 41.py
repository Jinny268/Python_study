# 40번의 업그레이드 버전
# 삼선승제 가위바위보 게임
print("### 안나와 신후의 가위, 바위, 보 게임 ###")
print('삼선승제로 세판 먼저 이기는 사람이 승리!!')
print('-----------------------------------------')

win_a = 0
win_b = 0

while win_a <3 and win_b <3:

  user_a = input("안나를 위한 가위, 바위, 보를 입력하세요: ")
  user_b = input("신후를 위한 가위, 바위, 보를 입력하세요: ")

  if user_a == '가위':

    if user_b == '가위':
      print('무승부')

    elif user_b == '바위':
      print('신후 승리')
      win_b += 1

    elif user_b =='보':
      print('안나 승리')
      win_a += 1

    else:
      print("신후 값 입력 오류 ->",user_b)
    
    

  elif user_a == '바위':

    if user_b == '가위':
      print('안나 승리')
      win_a += 1

    elif user_b == '바위':
      print('무승부')
    
    elif user_b =='보':
      print('신후 승리')
      win_b += 1

    else:
      print("신후 값 입력 오류 ->",user_b)

      
      
  elif user_a == '보':

    if user_b == '가위':
      print('신후 승리')
      win_b += 1

    elif user_b == '바위':
      print('안나 승리')
      win_a += 1

    elif user_b =='보':
      print('무승부')

    else:
      print("신후 값 입력 오류 ->",user_b)

      

  else:
    print("안나 값 입력 오류->",user_a)

    

  print('안나',win_a,':','신후',win_b)

if win_a == 3:
  print("### 안나 3선승! 최종 승리!! ###")
else:
  print("### 신후 3선승! 최종 승리!! ###")
