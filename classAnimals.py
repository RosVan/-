class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def printCat(self):
        print("Имя:", self.name,'|', "Пол:", self.gender,'|', 'Возраст:', self.age,'года(лет)')

class Dog:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def printDog(self):
        print("Имя:", self.name,'|', "Пол:", self.gender,'|', 'Возраст:', self.age,'года(лет)')

