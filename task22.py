#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы, с помощью шифра Цезаря.
# Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются.
# Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.



def code(string, n):
    answ = list()
    i = 0
    while i < len(string):
        if string[i].isalpha() != True:# Спецсимволы
            answ.append(string[i])
        else:# Буквы
            if string[i].isupper() == True:# Заглавные буквы
                new_let_pos = ABC_str.find(string[i]) + n
                if new_let_pos <= (len(ABC_str) - 1):# Если не выходит за диапазон алфавита
                    answ.append(ABC_str[new_let_pos])
                    # print(answ)
                else:# Если выходит за диапазон алфавита
                    answ.append(ABC_str[new_let_pos - len(ABC_str)])
                    # answ.append(chr(len(ABC_str)))
            else:# Строчные буквы
                new_let_pos = abc_str.find(string[i]) + n
                if new_let_pos <= (len(abc_str) - 1):# Если не выходит за диапазон алфавита
                    answ.append(abc_str[new_let_pos])
                else:# Если выходит за диапазон алфавита
                    answ.append(abc_str[new_let_pos - len(abc_str)])
        i += 1
    answ_str = ''.join(answ)
    return answ_str


ABC_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc_str = 'abcdefghijklmnopqrstuvwxyz'

str_in = str(input('Введите строку (латинские буквы):   '))
N_in = int(input('Введите сдивг (целое число): '))

# str_in = 'Hello, Cesar XYZ xyz!'
# N_in = 1000
N = N_in
while N >= len(ABC_str):
    N = N - len(ABC_str)



print('')
print('Исходная строка: ', str_in)
print('Заданный сдвиг (количество позиций): ', N_in)
if N != N_in:
    print('Реальный сдвиг (количество позиций): ', N)
print('Изменённая строка: ', code(str_in, N))