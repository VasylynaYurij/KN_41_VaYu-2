# Перевірка assert
number = -1
try:
    assert number > 0, "Число має бути більшим за нуль!"
except AssertionError as e:
    print(f"Помилка: {e}")

