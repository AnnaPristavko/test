# объявление функции
def is_password_good(password):
    counter = 0
    for i in password:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            counter += 1
            break
    for i in password:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            counter += 1
            break
    for i in password:
        if i in '0123456789':
            counter += 1
            break
    if (counter == 3) and (len(password) > 7):
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))