# 숫자를 입력받아 오름차순으로 정렬하기
cards=[]

card=int(input('Please enter an integer (enter 0 to exit): '))
while card != 0:
    cards.append(card)
    card=int(input('Please enter an integer (enter 0 to exit): '))

cards.sort()

for card in cards:
    print(card)
