#todo:
#  Реализуйте функцию convert(), которая принимает один аргумент:
#  number — целое число
#  Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
#  двоичное представление числа number в виде строки без префикса 0b
#  восьмеричное представление числа number в виде строки без префикса 0o
#  шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
#  Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().
#  Задачу решить доступным способом
#  Задачу решить с помощью применения функции map и lambda

dig_in = int(input('Введите целое число: ', ))
# dig_in = 125

def convert(def_in):
    tuple_out = (''.join(list(bin(def_in))[2:]), ''.join(list(oct(def_in))[2:]), ''.join(list(hex(def_in))[2:]).upper())
    return tuple_out

print(convert(dig_in))
