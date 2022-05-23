# 리스트 안에 있는 숫자 2개를 중복을 허용하여 선정한 뒤 더하는 경우의 수 모두 출력하기
numbers = ['1','2','3','4','5','6']
for die_1 in numbers:
  for die_2 in numbers:
    print(die_1,'+',die_2,'=',int(die_1)+int(die_2))
