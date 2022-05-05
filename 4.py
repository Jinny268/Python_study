text=input('영어 대소문자로 이루어진 문장을 입력하세요.\n')

print('\n모두 대문자로 변경\n'+text.upper())   # upper()를 사용하여 대문자로 변경

print('\n모두 소문자로 변경\n'+text.lower())   # lower()를 사용하여 대문자로 변경

# for문을 사용하여 대소문자 변경
new_text=str()
for c in text:
    if c.islower():
        new_text+=c.upper()
    else:
        new_text+=c.lower()
print('\nfor문과 if문을 사용하여 대소문자 변경\n'+new_text)

print('\n소스코드 한 줄로 대소문자 변경\n'+text.swapcase())   # swapcase()를 이용하여 한 줄로 대소문자 변경
