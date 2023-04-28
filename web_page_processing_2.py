'''
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. 
В этой статье есть теги code, которыми выделяются конструкции на языке Python. 
Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке, 
разделяя пробелами.

Например, если исходный текст страницы выглядел бы так:
<code>a</code>
<a>bracadabr</a>
<code>c</code>
<code>b</code>
<code>b</code>
<code>c</code>
то в ответ надо было бы ввести строку "b c".
'''

from urllib.request import urlopen # для открытия URL
from collections import Counter # для посчета совпадений (выводит инфу в объект типа Counter, подклас словаря)
from pprint import pprint #для печати объекта типа
import re # регулярные выражения


pattern = r'<code>(.*?)</code>'
url = 'https://stepik.org/media/attachments/lesson/209719/2.html'
html = urlopen(url).read().decode('utf-8')
data = str(html)
find_all = sorted(re.findall(pattern, data))
cnt = Counter(find_all)

pprint(cnt)

# вариант два
import requests, collections, re, pprint
res = requests.get(' https://stepik.org/media/attachments/lesson/209719/2.html').text
pprint.pprint(collections.Counter(re.findall(r'<code>(.*?)</code>', res)))
