# 과목 별 점수를 입력받아 성적표 보여주기
print('3개 과목의 시험 점수를 차례대로 입력하세요!')
국어=input('국어: ')
영어=input('영어: ')
수학=input('수학: ')
print('====================')
print('===시험 점수 결과===')
print('====================')
print('*국어 점수:', str(국어))
print('*영어 점수:', str(영어))
print('*수학 점수:', str(수학))
print('====================')
합계=int(국어)+int(영어)+int(수학)
평균=round(int(합계)/3, 2)
print('*총 합계 점수:', str(합계))
print('*평균 점수:', str(평균))
print('====================')

