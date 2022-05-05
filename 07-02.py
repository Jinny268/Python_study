text=input('문자열을 입력하세요 : ')

origin = text.replace(' ','')
reverse=str()

index=len(origin)-1

while index>=0:
    reverse+=origin[index]
    index-=1

if origin==reverse:
    print('입력하신 문장은 화문이 맞습니다.')

else:
    print('입력하신 문장은 화문이 아닙니다.')
