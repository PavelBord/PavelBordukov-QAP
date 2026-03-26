# # 1. Напиши функцию copy_file(source: str, destination: str) -> bool которая читает содержимое
# # файла source и записывает его в destination.
# # Возвращает True если успешно. Проверь что файл-копия создался.

import os


def copy_file(source: str, destination: str) -> bool:
    try:
        with open(source, "r") as src:
            read_1 = src.read()
        with open(destination, "w") as dest:
            dest.write(read_1)
        return True
    except Exception as e:
        print(f"Ошибка при копирование: {e}")
        return False


sou_name = "grades.txt"
dest_name = "grades_copy.txt"

if copy_file(sou_name, dest_name):
    if os.path.exists(dest_name):
        print(f"Успех! Файл '{dest_name}' создан")

# Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:
# Анна,85
# Иван,72
# Петр,91
# Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично'
# если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'.
# Сохрани результат в новый файл grades_with_status.txt.


with open("grades.txt", "w") as f:
    f.write("Анна,85\nИван,72\nПетр,91")

with (
    open("grades.txt", "r") as f_in,
    open("grades_with_status.txt", "w") as f_out,
):
    for line in f_in:
        name, score = line.strip().split(",")
        s = int(score)

        status = "Отлично" if s >= 90 else "Хорошо" if s >= 75 else "Удовлетворительно"

        f_out.write(f"{name},{score},{status} \n")


# 3. Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает
# дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет.

from datetime import datetime, timezone


def age_calculator(birth_date_str: str) -> int:
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
    today = datetime.now(timezone.utc)

    return (today.year - birth_date.year) - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


use_input = input("Введите дату рождения в формате д/м/г: ")
age = age_calculator(use_input)
print(f"Полных лет: {age}")


# 4.Напиши модуль file_utils.py с тремя полностью аннотированными функциями:
# def read_lines(filename): ...
# def write_lines(filename, lines): ...
# def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь.
# В main.py импортируй и протестируй все три.

# 5. Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password).
# Вложенная принимает пароль и возвращает True если совпадает, иначе False.
# Внешняя переменная с паролем не должна быть доступна снаружи

from typing import Callable


def password_checker(correct_password: str) -> Callable[[str], [bool]]:

    def check(password: str) -> bool:
        return password == correct_password

    return check


verify = password_checker("Pav1234")

print(verify("admin"))
print(verify("Pav1234"))

