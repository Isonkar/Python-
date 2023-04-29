'''
В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица.
Просуммируйте все числа в ней.
Теперь мы добавили разных тегов для изменения стиля отображения. 
Для доступа к ячейкам используйте возможности BeautifulSoup.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup


link = 'https://stepik.org/media/attachments/lesson/209723/4.html'


def get_data(url):
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def processing(data):
    res = 0
    for item in data.find_all('td'):
        res += int(item.text)
    return res


print(processing(get_data(link)))

