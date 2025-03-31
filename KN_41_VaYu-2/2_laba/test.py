from app import Figure

def test_get_angles():
    """Тестуємо чи правильно повертається кількість кутів фігури."""
    fig = "трикутник"
    triangle = Figure(fig, 1)
    assert triangle.get_angles == 3, f"У {fig} є 3 кути!"

class Figure:
    def __init__(self, type, sides):
        self.type = type
        self.sides = sides

    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3
