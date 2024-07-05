def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list = [1, 3.45, 'loft']
values_dict = {'a': 'dog', 'b': 76, 'c': 8.98}
values_list_2 = [5789, 'пароль от номера квартиры']

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)