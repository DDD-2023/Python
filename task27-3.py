#todo:
# Создайте лямбда функцию, которая принимает один параметр – строку.
# Переводит все буквы в нижний регистр и переворачивает их в обратном порядке. Пример входа: ‘ACbdzYx’,
# Вывод: 'xyzdbca'


# str_in = 'ABCdef123'#.lower()
str_in = input('Введите строку: ')#.lower()

# str_end = ''.join(list(reversed(list(map(lambda x: str_lower[x], range(len(str_lower)))))))# Работает
# print(str_end)@ Работает

# str_end = ''.join(list(reversed(list(map(lambda x: str_lower[x], range(len(str_lower)))))))# Тест

lam_fun = lambda x: (''.join(list(reversed(list(x.lower())))))

print(lam_fun(str_in))