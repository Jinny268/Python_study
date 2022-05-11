mag=float(input('Please enter the magnitude of the earthquake: '))

if mag<2:
    print('A magnitude %0.1f earthquake is considered to be a micro earthquake.' %mag)
elif 2<=mag<3:
    print('A magnitude %0.1f earthquake is considered to be a very minor earthquake.' %mag)
elif 3<=mag<4:
    print('A magnitude %0.1f earthquake is considered to be a minor earthquake.' %mag)
elif 4<=mag<5:
    print('A magnitude %0.1f earthquake is considered to be a light earthquake.' %mag)
elif 5<=mag<6:
    print('A magnitude %0.1f earthquake is considered to be a moderate earthquake.' %mag)
elif 6<=mag<7:
    print('A magnitude %0.1f earthquake is considered to be a strong earthquake.' %mag)
elif 7<=mag<8:
    print('A magnitude %0.1f earthquake is considered to be a major earthquake.' %mag)
elif 8<=mag<9:
    print('A magnitude %0.1f earthquake is considered to be a great earthquake.' %mag)
