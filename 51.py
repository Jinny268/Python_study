a=input('당신의 학점을 입력해주세요: ')

if a=='A+' or a=='A':
    print('%s, 이 학점의 점수는 4.0점입니다.' %a)
elif a=='A-':
    print('%s, 이 학점의 점수는 3.7점입니다.' %a)
elif a=='B+':
    print('%s, 이 학점의 점수는 3.3점입니다.' %a)
elif a=='B':
    print('%s, 이 학점의 점수는 3.0점입니다.' %a)
elif a=='B-':
    print('%s, 이 학점의 점수는 2.7점입니다.' %a)
elif a=='C+':
    print('%s, 이 학점의 점수는 2.3점입니다.' %a)
elif a=='C':
    print('%s, 이 학점의 점수는 2.0점입니다.' %a)
elif a=='C-':
    print('%s, 이 학점의 점수는 1.7점입니다.' %a)
elif a=='D+':
    print('%s, 이 학점의 점수는 1.3점입니다.' %a)
elif a=='D':
    print('%s, 이 학점의 점수는 1.0점입니다.' %a)
elif a=='F':
    print('%s, 이 학점의 점수는 0점입니다.' %a)
else:
    print('잘못된 입력입니다.')
