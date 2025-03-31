# Перевірка assert
number = -1
assert number > 0, "Число має бути більшим за нуль!"

# Введення числа з клавіатури
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"Введене число: {a}")

# Клас Figure з assert для валідації
types_allowed = ["квадрат", "прямокутник", "трикутник"]
class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in types_allowed, f"Дозволені фігури: {', '.join(types_allowed)}"
        self.type = type
        self.length = length

# Перевірка створення об'єктів
fig1 = Figure("квадрат", 1)
# fig2 = Figure("трапеція", 12)  # Викине помилку
# fig3 = Figure("квадрат", 0)  # Викине помилку

# Клас Name з ValueError для перевірки імені та хобі
names_allowed = ["Богдан", "Анонім", "Юрій"]
class Name:
    def __init__(self, name, hobby) -> None:
        if name not in names_allowed:
            raise ValueError(f"Дозволені імена: {', '.join(names_allowed)}")
        if not hobby:
            raise ValueError("Хобі не може бути порожнім!")
        self.name = name
        self.hobby = hobby

# Перевірка створення об'єктів
person1 = Name("Юрій", "Програмування")
# person2 = Name("Бодько", "")  # Викине помилку
# person3 = Name("Артем", "Музика")  # Викине помилку
