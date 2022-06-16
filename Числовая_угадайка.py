import random

def is_valid(s): # проверка введенных значений
    return s.isdigit() and 1<=int(s)<=100 and float(s) - int(float(s)) == 0

def input_number(): # ввод данных
    while True:
        guess = input()
        if is_valid(guess):
            return int(guess)
        else:
            print('Введите пожалуйста целое число от 1 до 100:')


def compare_number(down_num, up_num):  # Сравнение с загаданным
    number = random.randint(down_num, up_num)
    counter=0
    while True:
        s = input_number()
        counter+=1
        if s<number:
            print('Ваше число меньше загаданного, продолжайте угадывать')
        elif s>number:
            print('Ваше число больше загаданного, продолжайте угадывать')
        elif s==number:
            print('Вы угадали, поздравляю!')
            print('количество попыток:', counter)
            break

def continue_game(): 
    ans = input('Еще раз? ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Еще раз? ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('Спасибо за игру! Приходите снова')
            return False
        else:
            return True

def game(): # Запуск игры
    print('Добро пожаловать в числовую угадайку!')
    while True:
        print('Укажите диапазон в пределах от 1 до 100:')
        x, y = input_number(), input_number()
        if x > y:
            x, y = y, x
        print('Введите число от', x, 'до', y, '\n')
        compare_number(x, y)
        if continue_game():
            continue
        else:
            break

game() # Вызов игры


