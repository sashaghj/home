import random


name = input('Привет, как тебя зовут?')

print(f'Хорошо,{name},это генератор паролей любой сложности')

otmena = print('для отмены отправь 0')

chars = './abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = input('количество паролей?'+ "\n")

length = input('длина пароля?'+ "\n")


number = int(number)

length = int(length)

for n in range(number):
    password =''
    for i in range(length):
         password += random.choice(chars)
    print(password)