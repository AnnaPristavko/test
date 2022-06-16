# объявление функции
def convert_to_python_case(text):
    ns = text[0].lower()
    for i in range(1,len(text)):
        if text[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ns += '_'+text[i].lower()
        else:
            ns+=text[i]
    return ns

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))