en_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
ru_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def is_valid_direction():
    while True:
        direction = input('Выбери "ш" для шифрования или "д" для дешифрования текста\n')
        if direction=='ш':
            return True
        elif direction=='д':
            return False
        else:
            print('Введите либо "д" либо "ш", ну что не ясно,а?')

def is_valid_language():
    while True:
        language = input('Выберите язык ("рус"/"анг")?\n')
        if language=='рус':
            return True
        elif language=='анг':
            return False
        else:
            print('Введите либо "рус" либо "анг", других языков тут нет!')

def encryption(text):
    new_text = ''
    if l:
        for i in range(len(text)):
            if text[i] in ru_lower_alphabet:
                if (ru_lower_alphabet.find(text[i]) + step) >= len(ru_lower_alphabet):
                    new_text += ru_lower_alphabet[ru_lower_alphabet.find(text[i]) + step - 32]
                else:
                    new_text += ru_lower_alphabet[ru_lower_alphabet.find(text[i]) + step]
            elif text[i] in ru_upper_alphabet:
                if (ru_upper_alphabet.find(text[i]) + step) >= len(ru_upper_alphabet):
                    new_text += ru_upper_alphabet[ru_upper_alphabet.find(text[i]) + step - 32]
                else:
                    new_text += ru_upper_alphabet[ru_upper_alphabet.find(text[i]) + step]
            else:
                new_text += text[i]
    else:
        for i in range(len(text)):
            if text[i] in en_lower_alphabet:
                if (en_lower_alphabet.find(text[i]) + step) >= len(en_lower_alphabet):
                    new_text += en_lower_alphabet[en_lower_alphabet.find(text[i]) + step - 26]
                else:
                    new_text += en_lower_alphabet[en_lower_alphabet.find(text[i]) + step]
            elif text[i] in en_upper_alphabet:
                if (en_upper_alphabet.find(text[i]) + step) >= len(en_upper_alphabet):
                    new_text += en_upper_alphabet[en_upper_alphabet.find(text[i]) + step - 26]
                else:
                    new_text += en_upper_alphabet[en_upper_alphabet.find(text[i]) + step]
            else:
                new_text += text[i]
    return new_text

def decryption(text):
    new_text = ''
    if l:
        for i in range(len(text)):
            if text[i] in ru_lower_alphabet:
                new_text += ru_lower_alphabet[ru_lower_alphabet.find(text[i]) - step]
            elif text[i] in ru_upper_alphabet:
                new_text += ru_upper_alphabet[ru_upper_alphabet.find(text[i]) - step]
            else:
                new_text += text[i]
    else:
        for i in range(len(text)):
            if text[i] in en_lower_alphabet:
                new_text += en_lower_alphabet[en_lower_alphabet.find(text[i]) - step]
            elif text[i] in en_upper_alphabet:
                new_text += en_upper_alphabet[en_upper_alphabet.find(text[i]) - step]
            else:
                new_text += text[i]
    return new_text

def start_decryptor():
    while True:
        global d
        d = is_valid_direction()
        global l
        l = is_valid_language()
        global step
        step = int(input('Введите шаг сдвига(число)\n'))
        global text
        text = input('Введите текст\n')
        if d:
            print(encryption(text))
            break
        else:
            print(decryption(text))
            break

start_decryptor()