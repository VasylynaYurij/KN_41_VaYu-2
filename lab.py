# simple_calculator.py

def add(a, b):
    """Функція для додавання двох чисел."""
    return a + b

# main.py
from simple_calculator import add

# Викликаємо функцію для тесту
if __name__ == "__main__":
    result = add(3, 5)
    print(f"Результат додавання: {result}")

# test_simple_calculator.py

from simple_calculator import add

def test_add():
    """Тест для функції додавання"""
    assert add(1, 2) == 3, "Додавання 1 + 2 має дорівнювати 3"
    assert add(-1, 1) == 0, "Додавання -1 + 1 має дорівнювати 0"
    assert add(0, 0) == 0, "Додавання 0 + 0 має дорівнювати 0"
    assert add(-3, -2) == -5, "Додавання -3 + (-2) має дорівнювати -5"
