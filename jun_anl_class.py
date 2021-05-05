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
                if self.denominator != other.denominator:
                    # приводим обе дроби к единому знаменателю
                    # по-хорошему надо приводить к наименьшему общему знаменателю, но лень :)
                    self.numerator *= other.denominator
                    other.numerator *= self.denominator
                    self.denominator *= other.denominator
                    other.denominator = self.denominator

                # складываем числители и выводим итоговый результат
                result = Fraction(self.numerator + other.numerator, self.denominator)
                return result
            else:
                return 'Ошибка ввода данных'
        result = Fraction(numerator, denominator)
        return result



number_1 = Fraction(1, 3)
number_2 = Fraction(1, 6)
print(number_1 + number_2)
