#todo:
# Создайте лямбда функцию, которая принимает один параметр – строку.
# Переводит все буквы в нижний регистр и переворачивает их в обратном порядке. Пример входа: ‘ACbdzYx’,
# Вывод: 'xyzdbca'



# str_in = 'ABCdef'
str_lower = input('Введите строку: ').lower()
lst_in = list(str_lower)

lst_end = []

for i in range((len(lst_in)-1), -1, -1):
    lst_end.append(lst_in[i])

str_end = ''.join(lst_end)

print(str_end)