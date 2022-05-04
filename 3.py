'''
# 리스트를 이용한 반복문
colors = ['black', 'blue', 'yellow', 'red']   # 리스트 선언

for color in colors:   # 반복문
    print(color, len(color))
'''

# 가위-바위-보 리스트 선언
all = ['가위', '바위', '보']

# 바깥쪽 for문
for user_a in all:

    # 안쪽 for문
    for user_b in all:

        # 결과 출력
        print(user_a, 'VS', user_b)
