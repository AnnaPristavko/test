# объявление функции
def is_palindrome(text):
    dir_or = ''.join([i.lower() for i in list(text) if i.isalpha()])
    if dir_or==dir_or[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))