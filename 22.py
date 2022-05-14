a=float(input('당신의 점수를 숫자로 입력하세요: '))

if a>=4.0:
    print('%f점은 A+ 입니다.' %a)
elif 3.85 <a< 4.0:
    print('%f점은 A 입니다.' %a)
elif 3.5<a<=3.85:
    print('%f점은 A- 입니다.' %a)
elif 3.15<a<=3.5:
    print('%f점은 B+ 입니다.' %a)
elif 2.85<a<=3.15:
    print('%f점은 B 입니다.' %a)
elif 2.5<a<=2.85:
    print('%f점은 B- 입니다.' %a)
elif 2.15<a<=2.5:
    print('%f점은 C+ 입니다.' %a)
elif 1.85<a<=2.15:
    print('%f점은 C 입니다.' %a)
elif 1.5<a<=1.85:
    print('%f점은 C- 입니다.' %a)
elif 1.15<a<=1.5:
    print('%f점은 D+ 입니다.' %a)
elif 0.5<a<=1.15:
    print('%f점은 D 입니다.' %a)
elif 0<=a<=0.5:
    print('%f점은 D 입니다.' %a)
else:
    print('잘못된 입력입니다.')
