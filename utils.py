import json
from datetime import datetime


def get_correct_date(data: str):
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
                    i['date'] = get_correct_date(value)

    res.sort(key=lambda x: datetime.strptime(x.get('date', '2000-01-01 00:00'), "%Y-%m-%d %H:%M"), reverse=True)
    return res
