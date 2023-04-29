'''
В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица. 
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму. 
Для доступа к ячейкам используйте возможности BeautifulSoup.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html').read().decode('utf-8')
data = str(html)  # к строке можно не приводить, и так работает
soup = BeautifulSoup(data, 'html.parser')

res = 0
for item in soup.find_all('td'):
    res += int(item.get_text())  # можно заменить на item.text

print(res)

# вариант два
from urllib.request import urlopen
from bs4 import BeautifulSoup

soup = BeautifulSoup(urlopen("https://stepik.org/media/attachments/lesson/209723/3.html"), "html.parser")
print(sum([int(i.text) for i in soup.find_all("td", text=True)]))
