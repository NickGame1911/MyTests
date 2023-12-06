import pytest
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'

# Функция записи html файла
def get_html(url):
   response = requests.get(url)

   with open('test.html', 'w', encoding='utf-8') as html_file:
      return html_file.write(response.text)

# Функция чтения html файла
def read_html(file_name):
    with open(file_name, 'r', encoding='utf-8') as html_file:
      return html_file.read()

# DataClass для данных таблицы
@dataclass
class PLanguageTable:
   website: str               # Название сайта
   popularity: str            # Популярность
   frontend: str              # Клиентская часть
   backend: str               # Серверная часть
   database: str              # База данных
   notes: str                 # Примечания
   popularity_num: int = None # Популярность (числовое значение)

   # Функция для получения числового значения популярности
   def __post_init__(self):
      pop_num = ''

      for number in self.popularity:
         if number.isdigit():
            pop_num += number
         elif number != ',' and number != '.':
            break

      self.popularity_num = int(pop_num)

# Функция для получения данных таблицы из html файла
def parse_table(file_name):
   results = []
   soup = BeautifulSoup(read_html(file_name))

   for rows in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
      data = rows.find_all(['th','td'])

      website = data[0].a.text
      popularity = data[1].text
      frontend = data[2].text
      backend = data[3].text
      database = data[4].text
      notes = data[5].text

      results.append(PLanguageTable(website, popularity, frontend, backend, database, notes))

   return results

data = []
test_numbers = [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9]

# Формирования параметров для проведения тестирования
table = parse_table('test.html')
for test_number in test_numbers:
   for row in table:
      data.append((row.website, row.popularity_num, test_number))

# Функция для тестирования таблицы на наличие сайтов (строк) с популярностью меньше заданого значения
@pytest.mark.parametrize('website, popularity, param', data)
def test_table(website, popularity, param):
   assert popularity >= param, "{} has {} unique visitors per month. (Expected more than {})".format(website, popularity, param)