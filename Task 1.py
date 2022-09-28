# 1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import codecs

with open('Text.txt', 'r', encoding='utf-8') as f:
    read = f.readline()

text = ' '.join(list(filter(lambda x: "абв" not in x, read.split())))

print("Текст после удаления:", text)

f = open('final_data_tsk1.txt', "w")
f.write(text)
f.close()