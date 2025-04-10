# Перевірка числа
number = -1
if number <= 0:
    print("Помилка: Число має бути більшим за нуль!")
else:
    print(f"Число: {number}")

# Введення числа з клавіатури
a = input("Введіть число: ")
if not a.isdigit():
    print("Помилка: Потрібно ввести число!")
else:
    print(f"Введене число: {a}")

# Клас Figure для перевірки типу та довжини
types_allowed = ["квадрат", "прямокутник", "трикутник"]
class Figure:
    def __init__(self, type, length) -> None:
        if length <= 0:
            print("Помилка: Довжина має бути більшою за 0!")
        elif type not in types_allowed:
            print(f"Помилка: Дозволені фігури: {', '.join(types_allowed)}")
        else:
            self.type = type
            self.length = length
            print(f"Фігура: {self.type}, Довжина: {self.length}")

# Перевірка створення об'єктів
fig1 = Figure("квадрат", 1)
fig2 = Figure("трапеція", 12)  # Помилка
fig3 = Figure("квадрат", 0)  # Помилка

# Клас Name для перевірки імені та хобі
names_allowed = ["Богдан", "Анонім", "Юрій"]
class Name:
    def __init__(self, name, hobby) -> None:
        if name not in names_allowed:
            print(f"Помилка: Дозволені імена: {', '.join(names_allowed)}")
        elif not hobby:
            print("Помилка: Хобі не може бути порожнім!")
        else:
            self.name = name
            self.hobby = hobby
            print(f"Ім'я: {self.name}, Хобі: {self.hobby}")

# Перевірка створення об'єктів
person1 = Name("Юрій", "Програмування")
person2 = Name("Бодько", "")  # Помилка
person3 = Name("Артем", "Музика")  # Помилка
