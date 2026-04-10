import math
from dataclasses import dataclass

# Создай класс Circle с protected атрибутом _radius. Добавь @property для radius
# (с проверкой: радиус > 0), и вычисляемые свойства area и perimeter через @property -
# они должны пересчитываться автоматически при изменении радиуса.


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float | int) -> None:
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Радиус должен быть больше 0")

    @property
    def area(self) -> float:
        return math.pi * self._radius**2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius


c = Circle(10)
print(c.radius)
print(c.area)
print(c.perimeter)

c.radius = 15

# Создай класс Vector с атрибутами x и y. Реализуй магические методы __add__
# (сложение двух векторов), __str__ (вывод в формате "Vector(x, y)"), и __eq__ (сравнение).
# Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6).


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Vector):
            return NotImplemented
        return self.x == value.x and self.y == value.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 == Vector(1, 2))
print(v1 == v2)

# Создай класс Temperature с @property для celsius, fahrenheit и kelvin.
# При установке значения через любое свойство должны автоматически пересчитываться остальные.
# Хранить следует только одно внутреннее значение.


class Temperature:
    def __init__(self, celsius: int | float) -> None:
        self._celsius = float(celsius)

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float | int) -> None:
        self._celsius = float(value)

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float | int) -> None:
        self._celsius = (value - 32) * 5 / 9

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float | int) -> None:
        if value < 0:
            raise ValueError("Кельвин не может быть меньше 0")
        self._celsius = value - 273.15


t = Temperature(30)
print(t.celsius)
print(t.fahrenheit)
print(t.kelvin)
t.fahrenheit = 32
print(t.celsius)
t.kelvin = 290
print(t.celsius)

# 4. Используй @dataclass для создания класса Point с полями x: float и y: float.
# Добавь метод distance_to(other: Point) - расстояние до другой точки.
# Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to.


@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


@dataclass
class Point3D(Point):
    z: float

    def distance_to(self, other: "Point3D") -> float:
        return math.sqrt(
            (other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2
        )


p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1)
print(p2)
print(p1.distance_to(p2))
p3 = Point3D(0, 0, 0)
p4 = Point3D(1, 2, 2)
print(p3)
print(p4)
print(p3.distance_to(p4))

# Создай класс-итератор Countdown, который при итерации возвращает числа от start до 0.
# Реализуй __iter__ и __next__ (при исчерпании бросай StopIteration).
# Проверь в цикле for и через list().


class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for i in Countdown(5):
    print(i)
print(list(Countdown(7)))
c = Countdown(5)
print(list(c))
print(list(c))
