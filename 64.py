def pd(a):
    for i in range(len(a) // 2):
        if a[i] != a[-1 -i]:
            return False
        return True

a=input('Please enter a word: ')
print(pd(a))
