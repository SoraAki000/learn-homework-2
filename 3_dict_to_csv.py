"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    user_dict = [
        {"name": "Сергей", "age": 25, "job": "Безработный"},
        {"name": "Маша", "age": 25, "job": "Медсестра"},
        {"name": "Вася", "age": 28, "job": "Программист"},
        {"name": "Эдуард", "age": 48, "job": "Начальник"}
    ]
    with open('file.csv', "w", encoding="utf-8") as f:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(f, fields, delimiter=";", lineterminator='\n')
        writer.writeheader()
        for user in user_dict:
            writer.writerow(user)


if __name__ == "__main__":
    main()
