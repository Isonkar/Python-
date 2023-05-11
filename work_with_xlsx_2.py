'''
Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал зарплаты для разных интересные ему профессий. 
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245267/salaries.xlsx. 
Выведите название региона с самой высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива после его упорядочивания) 
и, через пробел, название профессии с самой высокой средней зарплатой по всем регионам. 
'''
import xlrd3


wb = xlrd3.open_workbook('salaries.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
dict_s = {}, dict_j = {}
for index in range(1, 8):
    dict_s[sh.row_values(index)[0]] = sh.row_values(index)[1:]
    dict_j[sh.col_values(index)[0]] = sh.col_values(index)[1:]
for region, salaries in dict_s.items():
    dict_s[region] = sorted(salaries)[3]
 for position, salaries in dict_j.items():
    dict_j[position] = sum(salaries)/len(salaries)  
print(max(dict_s, key=dict_s.get), max(dict_j, key=dict_j.get))


#  вариант два с pandas
import pandas as pd


data = pd.read_excel('salaries.xlsx', index_col=0)
print(data.median(axis=1).idxmax(), data.mean(axis=0).idxmax())

