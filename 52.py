# 피타고라스 정리
def pythagoras(a, b):
    print('Please enter the length of the hypotenuse: %d' %((a**2+b**2)**0.5))
a, b=input('Please enter two shorter sides of the triangle: ').split()
pythagoras(int(a), int(b))
