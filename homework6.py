# 1. Используя filter() и lambda,
# отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 != 0, list_1))

print(result)

# 2. Напишите функцию apply_operations(numbers, *operations), которая принимает список чисел и произвольное количество
# lambda-функций, последовательно применяя каждую ко всему списку.


from typing import List, Callable


def apply_operations(numbers: list[int], *operations: Callable) -> list[int]:

    for op in operations:
        numbers = [op(x) for x in numbers]
    return numbers


nums_1 = [1, 3, 4, 7]


result = apply_operations(nums_1, lambda x: x * 10, lambda x: x - 1, lambda x: x**2)

print(f"Исходный список: {nums_1}")
print(f"Результат: {result}")


#  Напишите генератор chunked(lst, size), который разбивает список на куски
# заданного размера и поочередно их выдает. Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5]

from typing import Generator


def chunked(lst: list[int], size: int) -> Generator[list[int], None, None]:
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


list_1 = [1, 4, 5, 7, 8, 9, 10]
chunk_size = 3

for chunk in chunked(list_1, chunk_size):
    print(chunk)


# 4. Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20.


from typing import Generator


def prime_numbers() -> Generator[int, None, None]:
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num
        num += 1


prime_1 = prime_numbers()
first_num = [next(prime_1) for _ in range(20)]
print(f"20 простых чисел: {first_num}")


# . Напишите функцию safe_convert(value, type_func), которая пытается преобразовать value с
# помощью переданной функции (например, int, float). При ошибке возвращает None.

from typing import Callable, TypeVar, Optional

T = TypeVar("T")


def safe_convert(value, type_func: Callable) -> Optional[T]:
    try:
        return type_func(value)
    except (ValueError, TypeError):
        return None


print(safe_convert("77", int))
print(safe_convert("dfgy", int))
print(safe_convert([5, 6, 7], float))
print(safe_convert("16.6", float))


# 6. Создайте собственный класс исключения NegativeNumberError. Напишите функцию sqrt_safe(n),
# которая считает квадратный корень из числа, но при отрицательном n
# выбрасывает NegativeNumberError с понятным сообщением.

import math
from typing import Union


class NegativeNumberError(Exception):
    pass


def sqrt_safe(n: float) -> float:
    if n < 0:
        raise NegativeNumberError(f"Ошибка: число {n} отрицательное.")
    return math.sqrt(n)


try:
    print(f"Корень из 30: {sqrt_safe(30)}")
    print(f"Корень из -10: {sqrt_safe(-10)}")
except NegativeNumberError as e:
    print(e)

# 7. Напишите функцию-калькулятор calculator(a, b, op), где op — строка ("+", "-", "*", "/"). Обработайте все возможные исключения:
# деление на ноль, неизвестная операция, некорректные типы аргументов.


from typing import Union


def calculator(a: int | float, b: int | float, op: str) -> float:
    try:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }
        result = ops[op](a, b)
        return float(result)

    except ZeroDivisionError:
        return "Ошибка деление на 0! "
    except KeyError:
        return f"Ошибка: операция '{op}' не поддерживается "
    except TypeError:
        return "Ошибка: аргументы должны быть числами (int или float)."


print(calculator(25, 2, "/"))
print(calculator(30, 0, "/"))
print(calculator(10, 2, "&"))
print(calculator("10", 2, "+"))
