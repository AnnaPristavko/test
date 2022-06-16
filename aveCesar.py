s = input()
en_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
en_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cs = s.split()
def word_len(s):
    word = ''
    for i in s:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz ':
            word += i
    return len(word)

def encryption(text, step):
    new_text = ''
    for j in text:
        if j in en_lower_alphabet:
            ind = en_lower_alphabet.find(j) + step
            if ind >= len(en_lower_alphabet):
                new_text+=en_lower_alphabet[ind - 26]
            else:
                new_text+=en_lower_alphabet[ind]
        elif j in en_upper_alphabet:
            ind = en_upper_alphabet.find(j) + step
            if ind >= len(en_upper_alphabet):
                new_text+=en_upper_alphabet[ind - 26]
            else:
                new_text+=en_upper_alphabet[ind]
        else:
            new_text+=j
    return new_text

s_cryp = ''
for i in range(len(cs)):
    st = word_len(cs[i])
    c_word = encryption(cs[i],st)
    s_cryp+=c_word+' '
print(s_cryp.rstrip())

