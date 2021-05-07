def check_registration(line):
    pass

def add_correct_data(list):
    with open('registrations_good.log.txt', 'w', encoding='utf-8') as file:
        for line in list:
            file.write(line + '\n')
            print(f'Added line {line}')
    file.close()


correct_data = []
incorrect_data = []

with open('registrations_.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line[:-1]
        try:
            if line[0] == 'О':
                correct_data.append(line)
        except:
            pass

add_correct_data(correct_data)
