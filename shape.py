class Shape:

    def __init__(self):
        self.Moh = 0
        self.mah = 0


class mostatil(Shape):

    def __init__(self, Tool, Arz):
        Shape.Moh = (Tool + Arz) * 2
        Shape.mah = Tool * Arz

    def show_Moh(self):
        return Shape.Moh

    def show_mah(self):
        return Shape.mah


class daiere(Shape):

    def __init__(self, shoa):
        Shape.Moh = (shoa * 2) * 3.14
        Shape.mah = (shoa * shoa) * 3.14

    def show_Moh(self):
        return Shape.Moh

    def show_mah(self):
        return Shape.mah


r = mostatil(2, 3)
print(f"mostatil Moh: {r.show_Moh()} mah: {r.show_mah()}")
c = daiere(1 / 3.14)
print(f"daiere Moh: {c.show_Moh()} mah: {c.show_mah()}")