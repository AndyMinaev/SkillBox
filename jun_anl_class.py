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

    def __int__(self):
        if (self.numerator % self.denominator) / self.denominator >= 0.5:
            return self.numerator // self.denominator + 1
        else:
            return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator


number_1 = Fraction(3, 2)
number_2 = Fraction(1, 4)
print('{} + {} = {}'.format(number_1, number_2, number_1 + number_2))
print('{} + {} = {}'.format(number_1, 2, number_1 + 2))
print('{} - {} = {}'.format(number_1, number_2, number_1 - number_2))
print('{} - {} = {}'.format(number_1, 2, number_1 - 2))
print('{} * {} = {}'.format(number_1, number_2, number_1 * number_2))
print('{} * {} = {}'.format(number_1, 2, number_1 * 2))
print('Приведение к целому числу дроби {} = {}'.format(number_1, number_1.__int__()))
print('Приведение к целому числу дроби {} = {}'.format(number_2, number_2.__int__()))
print('Приведение к числу с плавающей точкой дроби {} = {}'.format(number_1, number_1.__float__()))
print('Приведение к числу с плавающей точкой дроби {} = {}'.format(number_2, number_2.__float__()))
