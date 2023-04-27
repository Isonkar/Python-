'''
скрипт находит количество упоминаний о C++ на странице по ссылке
'''


from urllib.request import urlopen

html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
ans = []
state = 0

for char in s:
    if char == '<':
        state = 1
    if char == '>':
        state = 0
    elif state == 0:
        ans.append(char)
s = ''.join(ans)

print(s)
print(s.count('C++'))

# задание 1
# html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
# s = str(html)
# print(s.count('Python'))
# print(s.count('C++'))

