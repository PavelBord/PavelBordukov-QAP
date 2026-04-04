# Создай класс Library с атрибутом класса books = [] и методами add_book(title), remove_book(title) и show_books().
# Продемонстрируй, что список книг общий для всех объектов класса.


class Library:
    books: list[str] = []

    def add_book(self, title: str) -> None:
        self.books.append(title)

    def remove_book(self, title: str) -> None:
        if title in self.books:
            self.books.remove(title)
        else:
            print("Книга не найдена")

    def show_books(self) -> None:
        print(self.books)


lib1 = Library()
lib2 = Library()

lib1.add_book("Война и мир")
lib1.add_book("Муму")

lib2.show_books()
lib2.remove_book("Инферно")
lib2.show_books()
lib2.remove_book("Война и мир")
lib2.show_books()

# Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info().
# Дочерние классы Manager (добавляет department) и Developer (добавляет language).
# Каждый переопределяет get_info().


class Employee:
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def get_info(self) -> str:
        return f"{self.name}, зарплата: {self.salary}"

    def __str__(self) -> str:
        return self.get_info()


class Manager(Employee):
    department: str

    def __init__(self, name: str, salary: int, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def get_info(self) -> str:
        return f"{super().get_info()}, отдел: {self.department}"


class Developer(Employee):
    language: str

    def __init__(self, name: str, salary: int, language: str) -> None:
        super().__init__(name, salary)
        self.language = language

    def get_info(self) -> str:
        return f"{super().get_info()}, язык: {self.language}"


m = Manager("Павел", 6000, "IT")
d = Developer("Иван", 4000, "Python")


class Intern(Employee):
    duration: str

    def __init__(self, name: str, salary: int, duration: str) -> None:
        super().__init__(name, salary)
        self.duration = duration

    def get_info(self) -> str:
        return f"{super().get_info()}, стаж: {self.duration}"


intern = Intern("Леша", 3000, "4 месяца")

employees = [m, d, intern]

for emp in employees:
    print(emp)

# Реализуй класс Stack (стек) с протектед атрибутом _items = [] и
# методами push(item), pop(), peek() (посмотреть верхний элемент), is_empty() и size()


class Stack:
    def __init__(self):
        self._items: list[int] = []

    def push(self, item: int) -> None:
        self._items.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


stack = Stack()

stack.push(10)
stack.push(30)
stack.push(40)

print(stack.peek())
print(stack.pop())
print(stack.size())
print(stack.is_empty())

# Создай класс Vehicle с методом move(), выводящим "Moving...".
# Создай дочерние классы Car, Boat и Plane, каждый переопределяет
# move() по-своему. Напиши функцию start_journey(vehicle), которая вызывает move() у
# любого переданного транспорта - продемонстрируй полиморфизм.


class Vehicle:
    def move(self) -> str:
        return "Moving..."


class Car(Vehicle):
    def move(self) -> str:
        return "Driving..."


class Boat(Vehicle):
    def move(self) -> str:
        return "Sailing..."


class Plane(Vehicle):
    def move(self) -> str:
        return "Flying..."


def start_journey(vehicle: Vehicle) -> None:
    print(vehicle.move())


start_journey(Car())
start_journey(Boat())
start_journey(Plane())


# Создай класс Student с атрибутами name и grades (список оценок).
# Добавь методы add_grade(grade), average() (средняя оценка), highest() и lowest().
# Защити grades через одиночное подчёркивание.


class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self._grades = []

    def add_grade(self, grade: int) -> None:
        if not isinstance(grade, int):
            raise TypeError("Оценка должна быть целым числом")
        if not (0 <= grade <= 100):
            raise ValueError("Оценка должна быть в диапазоне от 0 до 100.")
        self._grades.append(grade)

    def average(self) -> float:
        if not self._grades:
            raise ValueError("Без оценок")
        return sum(self._grades) / len(self._grades)

    def highest(self) -> int:
        if not self._grades:
            raise ValueError("Без оценок")
        return max(self._grades)

    def lowest(self) -> int:
        if not self._grades:
            raise ValueError("Без оценок")
        return min(self._grades)

    def __repr__(self) -> str:
        return f"Student(name = {self.name!r}, grades = {self._grades})"

    def __lt__(self, other: "Student") -> bool:
        return self.average() < other.average()


s1 = Student("Петя")
s2 = Student("Максим")
s1.add_grade(75)
s1.add_grade(65)
s2.add_grade(80)
s2.add_grade(75)

students = [s1, s2]
students.sort()


print(students)
print(f"{s1.name}: {s1.average()}")
print(f"{s2.name}: {s2.average()}")

print(s1 > s2)
print(s1 < s2)
