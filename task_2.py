
# В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик
# смогли объяснить нашей поддержке, кого они имеют в виду(у преподавателей, например, часто учится несколько Саш),
# мы генерируем пользователям уникальные и легко произносимые имена.Имя у нас состоит из прилагательного,
# имени животного и двузначной цифры.В итоге получается, например, "Перламутровый лосось 77".
# Для генерации таких имен мы и решали следующую задачу:
# Получить с русской википедии список всех животных(Категория: Животные по алфавиту) и вывести количество
# животных на каждую букву алфавита. Результат должен получиться в следующем виде:
# А: 642
# Б: 412
# В: ....


import requests
from bs4 import BeautifulSoup
import re
animals = {}
page = 1
url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
while url:
    print(f'Page: {page}')
    page += 1
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    groups = soup.find_all('div', class_='mw-category-group')
    for group in groups:
        char = group.find('h3').text
        animal_items = [
            i.text for i in group.ul.find_all('a')]
        if char in animals.keys():
            animals[char] += animal_items
        else:
            animals[char] = animal_items
    url = soup.find('a', title="Категория:Животные по алфавиту",
                    href=re.compile(r'pagefrom'))
    if url:
        url = 'https://ru.wikipedia.org' + url['href']

for key, item in animals.items():
    print(f'{key}: {len(item)}')
