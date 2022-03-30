
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return f'(Координата x = {self.x}, Координата y = {self.y},' \
               f' Ширина прямоугольника = {self.width}, Высота прямоугольника = {self.height})'

amount_Rectangle = Rectangle(5, 10, 50, 100)
print(amount_Rectangle.get_area())
#---------------------------------------

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

area_Rectangle = Rectangle(50, 100)
print('Площадь прямоугольника', area_Rectangle.get_area(), 'едениц')

#--------------------------------

class Wallet:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname= surname
        self.balance = balance

    def wallet(self):
        return f'(Клиент {self.name} {self.surname} Баланс: {self.balance} руб.)'

new_wallet = Wallet('Иван', 'Петров', 50)
print(new_wallet.wallet())