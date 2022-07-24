import random


count_of_attemps = 0

num = random.randint(1, 100)

name = input('Привет как тебя зовут?')

print('Отлично,я загадал число,угадай',format(name))
while True:
    pipul = int(input('Напиши число'))

    count_of_attemps = count_of_attemps + 1

    if pipul > num:
        print('Твое число больше чем я загадал')

    if pipul < num:
        print('Твое число меньше чем я загадал')

    if pipul == num:
        print('Ты угадал')
        break

if pipul == num:
    print(f'Поздравляю. Вы угадали!\nКоличество попыток: {count_of_attemps}')



