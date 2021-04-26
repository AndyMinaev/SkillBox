class Pet:
    """ Домашнее животное """
    legs = 4
    has_tail = True

    def inspect(self):
        print('Всего ног:', self.legs)
        print('Хвост присутствует - ', 'да' if self.has_tail else 'нет')


class Cat(Pet):
    """ Кошка - домашнее животное """

    def sound(self):
        print('мяу!')


class Dog(Pet):
    """ Собака - домашнее животное """

    def sound(self):
        print('гав!')


class Hamster(Pet):
    """ Хомячок - домашнее животное """

    def sound(self):
        print('ццц')


print('Котик')
my_pet = Cat()
my_pet.inspect()
my_pet.sound()

print('Собачка')
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

print('Хомячок')
my_pet = Hamster()
my_pet.inspect()
my_pet.sound()