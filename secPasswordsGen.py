from random import *
digits =  '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

counter_passwords = int(input('Сколько паролей сгенерировать?\n'))
password_len = int(input('Укажите длину пароля\n'))
def with_digits():
    req = input('Должен ли пароль содержать цифры ("д"/"н")?\n')
    while True:
        if req not in ('y', 'д', 'n', 'н'):
            req = input('Пожалуйста ответьте "д" или "н"?\n Должен ли пароль содержать цифры ("д"/"н")?\n')
        elif req in ('n', 'н'):
            return False
        elif req in ('y', 'д'):
            return True

def with_uppercase_letters():
    req = input('Должен ли пароль содержать прописные буквы ("д"/"н")?\n')
    while True:
        if req not in ('y', 'д', 'n', 'н'):
            req = input('Пожалуйста ответьте "д" или "н"?\n Должен ли пароль содержать прописные буквы ("д"/"н")?\n')
        elif req in ('n', 'н'):
            return False
        elif req in ('y', 'д'):
            return True

def with_lowercase_letters():
    req = input('Должен ли пароль содержать строчные буквы ("д"/"н")?\n')
    while True:
        if req not in ('y', 'д', 'n', 'н'):
            req = input('Пожалуйста ответьте "д" или "н"?\n Должен ли пароль содержать строчные буквы ("д"/"н")?\n')
        elif req in ('n', 'н'):
            return False
        elif req in ('y', 'д'):
            return True

def with_punctuation():
    req = input('Должен ли пароль содержать символы !#$%&*+-=?@^_ ("д"/"н")?\n')
    while True:
        if req not in ('y', 'д', 'n', 'н'):
            req = input('Пожалуйста ответьте "д" или "н"?\n Должен ли пароль содержать символы !#$%&*+-=?@^_ ("д"/"н")?\n')
        elif req in ('n', 'н'):
            return False
        elif req in ('y', 'д'):
            return True
def no_n_symbols():
    req = input('Исключать ли неоднозначные символы il1Lo0O ("д"/"н")?\n')
    while True:
        if req not in ('y', 'д', 'n', 'н'):
            req = input('Пожалуйста ответьте "д" или "н"?\n Исключать ли неоднозначные символы il1Lo0O ("д"/"н")?\n')
        elif req in ('n', 'н'):
            return False
        elif req in ('y', 'д'):
            return True
if with_digits():
    chars+=digits
if with_uppercase_letters():
    chars+=uppercase_letters
if with_lowercase_letters():
    chars+=lowercase_letters
if with_punctuation():
    chars+=punctuation
if no_n_symbols():
    chars = ''.join([i for i in chars if i not in 'il1Lo0O'])

def generate_password(password_len, chars):
    for i in range(counter_passwords):
        password = sample(chars,password_len)
        print(''.join(password))

print(generate_password(password_len, chars))



