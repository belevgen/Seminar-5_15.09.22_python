# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(string):
    if string == '': return ''
    encoded = ''
    i = 0
    while i < len(string) - 1:
        counter = 1
        symbol = string[i]
        j = i
        while j < len(string) - 1:
            if string[j] == string[j + 1]:
                counter += 1
                j += 1
            else:
                break
        encoded += str(counter) + symbol
        i = j + 1
    return encoded


def decode(enc_string):
    if enc_string == '': return ''
    decoded = ''
    i = 0
    while i < len(enc_string) - 1:
        number = ""
        j = i
        while j < len(enc_string):
            if enc_string[j].isdigit():
                number += enc_string[j]
            else:
                symbol = enc_string[j]
                decoded += symbol * int(number)
                break
            j += 1
        i = j + 1
    return decoded


cryptic = encode('qwweeerrrrtyqwerty')
print(cryptic)
print(decode(cryptic))