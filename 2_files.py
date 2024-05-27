"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    words, content = 0, []
    with open("referat.txt", "r", encoding="utf-8") as f:
        for line in f:
            words += len(line.split())
            content.append(line.replace('.', '!'))
    full_text = ''.join(content)
    print(f"Длина {len(full_text)} символов")
    print(f"В файле {words} слова")
    with open("referat2.txt", "w", encoding="utf-8") as f:
        f.write(full_text)


if __name__ == "__main__":
    main()
