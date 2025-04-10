# Функція для перевірки чисел
def check_number(number):
    if number <= 0:
        return "Помилка: Число має бути більшим за нуль!"
    return f"Число: {number}"

# Введення числа
number = int(input("Введіть число: "))
print(check_number(number))

# Клас для перевірки фігур
class Figure:
    def __init__(self, type, length):
        self.types_allowed = ["квадрат", "прямокутник", "трикутник"]
        if length <= 0:
            print("Помилка: Довжина має бути більшою за 0!")
        elif type not in self.types_allowed:
            print(f"Помилка: Дозволені фігури: {', '.join(self.types_allowed)}")
        else:
            self.type = type
            self.length = length
            print(f"Фігура: {self.type}, Довжина: {self.length}")

# Створення фігур
fig1 = Figure("квадрат", 5)
fig2 = Figure("трапеція", 10)  # Помилка
fig3 = Figure("квадрат", 0)  # Помилка

# Клас для перевірки імен
class Name:
    def __init__(self, name, hobby):
        self.names_allowed = ["Богдан", "Анонім", "Юрій"]
        if name not in self.names_allowed:
            print(f"Помилка: Дозволені імена: {', '.join(self.names_allowed)}")
        elif not hobby:
            print("Помилка: Хобі не може бути порожнім!")
        else:
            self.name = name
            self.hobby = hobby
            print(f"Ім'я: {self.name}, Хобі: {self.hobby}")

# Створення об'єктів імен
person1 = Name("Юрій", "Програмування")
person2 = Name("Бодько", "")  # Помилка
person3 = Name("Артем", "Музика")  # Помилка
