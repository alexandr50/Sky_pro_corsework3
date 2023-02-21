import json
from datetime import datetime
from pprint import pprint

FILE_NAME = 'data_file.json'


def get_correct_date_for_sort(data: str):
    """Функция преобразующая формат даты"""
    correct_data = data.replace('T', ' ')[:-10]
    return correct_data


def sorted_func_for_date(file):
    """Функция читающая из файла и сортирующая список по дате в словаре"""

    with open(file, 'r', encoding='utf-8') as file:
        res = json.load(file)
        for i in res:
            for key, value in i.items():
                if key == 'date':
                    i['date'] = get_correct_date_for_sort(value)

    res.sort(key=lambda x: datetime.strptime(x.get('date', '2000-01-01 00:00'), "%Y-%m-%d %H:%M"), reverse=True)
    return res


def correct_date_for_output(date):
    """Функция преобразующая формат даты для вывода пользователю"""

    correct_date = date.split(' ')
    result = '.'.join(correct_date[0].split('-')[::-1])
    return result


def correct_number_card(card):
    """Функция для корректного отображения карты клиента"""
    if card:
        number = card[-16:]
        word = card[:-17]
        number_for_output = ''
        for i, j in enumerate(number):
            if 6 <= i <= 12 and i % 4 != 0:
                number_for_output += '*'
            elif i % 4 == 0 and i != 0:
                if 6 <= i <= 11:
                    number_for_output += ' '
                    number_for_output += '*'
                else:
                    number_for_output += ' '
                    number_for_output += j
            else:
                number_for_output += j
        return f'{word} {number_for_output}'
    return ''

def get_correct_bill(bill):
    """Функция для корректного отображения счета"""
    end = 0
    for i, j in enumerate(bill):
        if j.isdigit():
            end = i - 1
            break
    return f'{bill[:end]} **{bill[-4:]}'




