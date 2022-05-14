# 가시광선 파장에 따른 빛의 색 알아보기
a=int(input('Please enter the wavelength of visible light(The unit is nm.): '))

if 380<=a<450:
    print('The color of this visible light is violet.')
elif 450<=a<495:
    print('The color of this visible light is blue.')
elif 495<=a<570:
    print('The color of this visible light is green.')
elif 570<=a<590:
    print('The color of this visible light is yellow.')
elif 590<=a<620:
    print('The color of this visible light is orange.')
elif 620<=a<750:
    print('The color of this visible light is red.')
else:
    print('The wavelength of visible light ranges from 380 to 750nm.')
