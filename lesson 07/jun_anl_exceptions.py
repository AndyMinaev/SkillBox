# -*- coding: utf-8 -*-

# Надо проверить данные из файла, для каждой строки:
#
# присутсвуют все три поля
# поле имени содержит только буквы
# поле email содержит @ и .
# поле возраст является числом от 10 до 99
# В результате проверки нужно сформировать два файла
#
# registrations_good.log для правильных данных, записывать строки как есть
# registrations_bad.log для ошибочных, записывать строку и вид ошибки.
# Для валидации строки данных написать метод, который может выкидывать исключения:
#
# НЕ присутсвуют все три поля: ValueError
# поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# поле email НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# поле возраст НЕ является числом от 10 до 99: ValueError Вызов метода обернуть в try-except.
class NotNameError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def add_correct_data(list):
    with open('registrations_good.log.txt', 'w', encoding='utf-8') as file:
        for line in list:
            file.write(line + '\n')
            print(f'Added line {line}')
    file.close()


def add_incorrect_data(list):
    with open('registrations_bad.log.txt', 'w', encoding='utf-8') as file:
        for line in list:
            file.write(line + '\n')
            print(f'Added line {line}')
    file.close()


def check_registration(name, email, age):
    if not name.isalpha():
        raise NotNameError(f'Invalid name {name}')
    if '@' not in email:
        raise NotEmailError('Incorrect email')
    if '.' not in email:
        raise NotEmailError('Incorrect email')
    age = int(age)
    if age < 10:
        raise ValueError('Age too small')
    if age > 99:
        raise ValueError('Age too large')


correct_data = []
incorrect_data = []
line_number = 0

with open('registrations_.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line_number += 1
        line = line[:-1]
        try:
            name, email, age = line.split(' ')
            check_registration(name=name, email=email, age=age)
            correct_data.append(line)
        except (ValueError, NotNameError, NotEmailError) as exc:
            incorrect_data.append('line #' + str(line_number) + ', ' + str(type(exc)) + ', ' + str(exc))
            print(f'Error at line #{line_number} - {exc}')

add_correct_data(correct_data)
add_incorrect_data(incorrect_data)
