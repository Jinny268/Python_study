# 회문 판별하기
line=input('Please enter a string: ')

i_p=True

for i in range(0, len(line)//2):
    if line[i]!=line[len(line)-i-1]:
        i_p=False

if i_p:
    print('%s is a palindrome.' %line)
else:
    print('%s is not a palindrome' %line)
