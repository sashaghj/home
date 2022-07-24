name = str(input('Привет, как тебя зовут?'))

print(f'Привет,{name}, это калькулятор')
print('Чтобы завершить операцию напиши Стоп')


x = float(input('Напиши первое число'))
y = float(input('Напиши второе число'))

while True:
    try:
        abc = input('Выбери операцию (+,-,*,/):')
        if abc == 'Стоп':
            break

        if abc == '+':
            print('Ваш ответ', x + y)

        if abc == '*':
            print(x * y)

        if abc == '/':
            print(x / y)

        if abc == '-':
            print(x - y)
    except:
        print('Введи операцию')

