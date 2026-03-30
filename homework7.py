import warnings
from typing import Callable
from functools import wraps

# Напишите рекурсивную функцию palindrome(s),
# которая проверяет, является ли строка палиндромом. Без срезов и reversed(), только рекурсия.


def palindrome(s: str, left: int = 0, right: int = None) -> bool:
    s = s.lower()

    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return palindrome(s, left + 1, right - 1)


print(palindrome("Vova"))
print(palindrome("acca"))
print(palindrome("Money"))

# Напишите функцию make_validator(min_val, max_val), которая возвращает функцию-валидатор.
# Валидатор принимает число и возвращает True если оно в диапазоне, иначе False.


def make_validator(min_val: int, max_val: int) -> Callable[[int], bool]:

    def validator(x: int) -> bool:
        return min_val <= x <= max_val

    return validator


age = make_validator(18, 60)
print(age(32))
print(age(67))

# Напишите декоратор @retry(n), который при возникновении любого исключения повторяет вызов функции до n раз.
# Если все попытки провалились — пробрасывает последнее исключение.


def retry[R, **P](n: int) -> Callable:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка {i + 1} провалилась {e} ")
                    if i == n - 1:
                        raise

        return wrapper

    return decorator


@retry(3)
def my_func():

    print("Выполняю...")
    raise ValueError("Упс!")


try:
    my_func()
except ValueError:
    print("Лимит исчерпан")

#  Напишите декоратор @deprecated(message), который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её.
# Сохраняйте метаданные через functools.wraps.


def deprecated[R, **P](message: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            warnings.warn(
                f"Функция {func.__name__} не рекомендуется к использованию! {message}",
                category=DeprecationWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator


warnings.simplefilter("always", DeprecationWarning)


@deprecated("Переходи на новую версию:")
def test():
    print("Выполняю")


test()


# Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке),
# оберните её декоратором @logger, который логирует каждый вызов с параметрами.


def logger[R, **P](func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:

        print(f"Вызов {func.__name__} с аргументами: args = {args}, kwargs = {kwargs} ")

        result = func(*args, **kwargs)

        print(f"Функция {func.__name__} вернула: {result} ")
        return result

    return wrapper


@logger
def binary_search(
    lst: list[int], target: int, low: int = 0, high: int | None = None
) -> int | None:
    if high is None:
        high = len(lst) - 1

    if low > high:
        return None

    mid = (low + high) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)

    else:
        return binary_search(lst, target, mid + 1, high)


numb = [15, 20, 35, 45, 55, 65, 75, 85, 90, 100]
print(f"Результат: {binary_search(numb, 90)}")
