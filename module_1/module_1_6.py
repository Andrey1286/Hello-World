my_dict = {'Andrey': 1986, 'Natalya': 1988, 'Alisa': 2016}
print(my_dict)
print(my_dict['Andrey'])
print(my_dict.get('Sasha'))
print(my_dict.get('Sasha', 'такого ключа нет'))
print(my_dict.get('Andrey'))
my_dict.update({'Sasha': 1985,
                'Aleksey': 1987})
print(my_dict)
x = my_dict.pop('Andrey')
print(x)
print(my_dict)

my_set = {1,2,3,4,5,1,2,3, 'Andrey', (1,2)}
print(my_set)
print(my_set.add(7))
print(my_set.add(6))
print(my_set)
print(my_set.remove('Andrey'))
print(my_set)