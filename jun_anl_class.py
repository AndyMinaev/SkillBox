class Fraction:

    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)


number_1 = Fraction(2, 5)
print(number_1)