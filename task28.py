#todo:
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda

lst_in = [123, 234, 345, 456]

lst_out = list(map(lambda x:sum(map(int, str(lst_in[x]))), range(len(lst_in))))
print(lst_out)