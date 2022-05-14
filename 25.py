hz=int(input('Please enter the frequency range(Hz): '))

if hz<3000000000:
    print('Radio waves!')
elif 3000000000<=hz<3000000000000:
    print('Microwaves!')
elif 3000000000000<=hz<430000000000000:
    print('Infrared light!')
elif 430000000000000<=hz<750000000000000:
    print('Visible light!')
elif 750000000000000<=hz<300000000000000000:
    print('Ultraviolet light!')
elif 300000000000000000<=hz<30000000000000000000:
    print('X-rays!')
elif 30000000000000000000<=hz:
    print('Gamma rays!')
