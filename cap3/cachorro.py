class Dog:
    def __init__(self, name):
        self.name = name

    def latir(self):
        print(f"{self.name} : woof woof")

my_dog = Dog('Bingo')

my_dog.latir()
