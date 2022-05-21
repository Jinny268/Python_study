#환전 대상 금액 입력
money=input('환전하고자 하는 금액을 입력하세요: ')

#각국 환율 적용 결과(정수 변환 후 소수점 셋째 자리에서 반올림)
usd=round(int(money)/1141.50, 2)
aud=round(int(money)/905.15, 2)
nzd=round(int(money)/836.15, 2)

#결과 출력
print('미국: ', usd, 'USD')
print('호주: ', aud, 'AUD')
print('뉴질랜드: ', nzd, 'NZD')
