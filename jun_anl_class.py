class Fraction:

    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):
        numerator = self.numerator
        denominator = self.denominator
        if isinstance(other, int):
            numerator += other * denominator
        else:
            if isinstance(other, Fraction):
                if denominator != other.denominator:
                    # приводим дробь к единому знаменателю, правда не меньшему, лень заморачиваться :)
                    numerator = numerator * other.denominator + other.numerator * denominator
                    denominator *= other.denominator
                result = Fraction(numerator, denominator)
                return result
            else:
                return 'Ошибка ввода данных'
        result = Fraction(numerator, denominator)
        return result

    def __radd__(self, other):
        numerator = self.numerator
        denominator = self.denominator
        if isinstance(other, int):
            numerator += other * denominator
        else:
            return 'Ошибка ввода данных'
        result = Fraction(numerator, denominator)
        return result

    def __sub__(self, other):
        numerator = self.numerator
        denominator = self.denominator
        if isinstance(other, int):
            numerator -= other * denominator
        else:
            if isinstance(other, Fraction):
                if denominator != other.denominator:
                    # приводим дробь к единому знаменателю, правда не меньшему, лень заморачиваться :)
                    numerator = numerator * other.denominator - other.numerator * denominator
                    denominator *= other.denominator
                # складываем числители и выводим итоговый результат
                result = Fraction(numerator, denominator)
                return result
            else:
                return 'Ошибка ввода данных'
        result = Fraction(numerator, denominator)
        return result

    def __rsub__(self, other):
        numerator = self.numerator
        denominator = self.denominator
        if isinstance(other, int):
            numerator = other * denominator - numerator
        else:
            return 'Ошибка ввода данных'
        result = Fraction(numerator, denominator)
        return result

    def __mul__(self, other):
        numerator = self.numerator
        denominator = self.denominator
        if isinstance(other, int):
            numerator *= other
        else:
            if isinstance(other, Fraction):
                numerator *= other.numerator
                denominator *= other.denominator
                result = Fraction(numerator, denominator)
                return result
            else:
                return 'Ошибка ввода данных'
        result = Fraction(numerator, denominator)
        return result

    def __rmul__(self, other):
        numerator = self.numerator
        denominator = self.denominator
        if isinstance(other, int):
            numerator *= other
        else:
            return 'Ошибка ввода данных'
        result = Fraction(numerator, denominator)
        return result

    def __int__(self):
        if (self.numerator % self.denominator) / self.denominator >= 0.5:
            return self.numerator // self.denominator + 1
        else:
            return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator


class OperationsOnFraction(Fraction):

    def getint(self):
        res = super().__int__()
        print('Приведение к целому числу дроби дочернего класса {} = {}'.format(self, res))

    def getfloat(self):
        res = super().__float__()
        print('Приведение к числу c плавающей точкой дроби дочернего класса {} = {}'.format(self, res))



number_1 = Fraction(3, 2)
number_2 = Fraction(1, 4)
# сложение
print('{} + {} = {}'.format(number_1, number_2, number_1 + number_2))
print('{} + {} = {}'.format(number_1, 2, number_1 + 2))
print('{} + {} = {}'.format(2, number_1, 2 + number_1))
print()

# вычитание
print('{} - {} = {}'.format(number_1, number_2, number_1 - number_2))
print('{} - {} = {}'.format(number_1, 2, number_1 - 2))
print('{} - {} = {}'.format(2, number_1, 2 - number_1))
print()

# умножение
print('{} * {} = {}'.format(number_1, number_2, number_1 * number_2))
print('{} * {} = {}'.format(number_1, 2, number_1 * 2))
print('{} * {} = {}'.format(2, number_1, 2 * number_1))
print()

# приведение к int и float
print('Приведение к целому числу дроби {} = {}'.format(number_1, number_1.__int__()))
print('Приведение к целому числу дроби {} = {}'.format(number_2, number_2.__int__()))
print('Приведение к числу с плавающей точкой дроби {} = {}'.format(number_1, number_1.__float__()))
print('Приведение к числу с плавающей точкой дроби {} = {}'.format(number_2, number_2.__float__()))
print()

# операции с дочерним классом
number_3 = OperationsOnFraction(4, 5)
number_3.getint()
number_3.getfloat()
