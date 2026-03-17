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