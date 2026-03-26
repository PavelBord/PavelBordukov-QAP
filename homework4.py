# Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры)
# в таком формате
# 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27


def table(x: int) -> None:
    print(*(x * i for i in range(1, 11)), sep=" | ")


x: int = int(input("Введите число: "))
table(x)

# 2.Попроси пользователя ввести имя и возраст.
# Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»


def future(name: str, age: int) -> None:
    new_age: int = age + 10
    print(f"Через 10 лет тебе будет {new_age} лет, {name}!")


user_name: str = input("Введите имя: ")
user_age: int = int(input("Введите возраст: "))

future(user_name, user_age)

# 3. Даны два списка цен в долларах и курс валюты.
# Используй map чтобы перевести все цены в рубли.
# Затем используй zip чтобы создать словарь {товар: цена_в_рублях}:

# items = ["хлеб", "молоко", "кофе"]
# prices_usd = [1.5, 2.0, 8.0]
# rate = 3.2


items: list[str] = ["хлеб", "молоко", "кофе"]
prices_usd: list[float] = [1.5, 2.0, 8.0]
rate: float = 3.2

prices_rub = map(lambda x: x * rate, prices_usd)

result: dict[str, float] = dict(zip(items, prices_rub))

print(result)

# 4.Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку:
# 'Fizz' если делится на 3, 'Buzz' если делится на 5, 'FizzBuzz' если делится на оба, иначе само число в виде строки.
# Вызови её для чисел от 1 до 20 через map.


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


numbers: range = range(1, 21)


result: list[str] = list(map(fizzbuzz, numbers))

print(result)


# 5.Напиши функцию *args с именем my_stats которая принимает любое количество чисел и
# возвращает сразу три значения — минимум, максимум и среднее.

from typing import Tuple


def my_stats(*args: float) -> Tuple[float, float, float]:
    minimum: float = min(args)
    maximum: float = max(args)
    summma: float = sum(args) / len(args)

    return minimum, maximum, summma


mn, mx, summ = my_stats(10, 20, 30, 40)
print(f"Мин: {mn}, Макс: {mx}, Среднее: {summ}")


# 6. Напиши функцию build_profile(**kwargs) которая принимает
# любые именованные аргументы и возвращает словарь с этими данными плюс автоматически
# добавляет ключ 'registered': True. Добавь к функции docstring.

from typing import Any


def build_profile(**kwargs: Any) -> dict[str, Any]:

    profile: dict[str, Any] = kwargs
    profile["registered"] = True
    return profile


user_name: str = input("Введите имя: ")
user_city: str = input("Введите город: ")


my_profile: dict[str, Any] = build_profile(name=user_name, city=user_city)

print(my_profile)


# 7.Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, cube(n) — возводит в куб, is_even(n) — возвращает True/False. В main.py импортируй модуль, 
# попроси пользователя ввести число через input, примени все три функции и выведи результаты. 
# Защити вызовы конструкцией if __name__ == "__main__".

import math_utils

def main() -> None:
    num: int = int(input("Введите целое число: "))

    sq: int = math_utils.square(num)
    cb: int = math_utils.cube(num)
    even: bool = math_utils.is_even(num)

    print(f"Квадрат: {sq}")
    print(f"Куб: {cb}")
    print(f"Четное: {even}")

if __name__ == "__main__":
    main()