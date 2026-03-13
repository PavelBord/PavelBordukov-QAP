n = int(input("Введите число: "))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
n = sum(int(d) ** 2 for d in str(n))
if n == 1:
    print("True")
else:
    print("False")
