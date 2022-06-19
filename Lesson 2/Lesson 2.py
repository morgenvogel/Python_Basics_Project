# Lesson_2

my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4], (5, 6, 6.5), {7: 'seven'}, frozenset(), range(11),
           b'twelve', bytearray(b'thirteen'), zip(*[(14, 15)])]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")

my_list = input('Enter the numbers with space: ').split()
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)

seasons_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
seasons_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
                10: 'осень', 11: 'осень', 12: 'зима', }
month = int(input('Введите номер месяца '))
if month in seasons_dict:
    print(seasons_list[month - 1])
    print(seasons_dict[month])
else:
    print('Нет такого месяца!')

s = input('Enter the words with space: ').split()
for i, word in enumerate(s, 1):
    print(i, word) if len(word) <= 10 else print(i, word[:10])

rating = [7, 5, 3, 3, 2]
print('Rating list is "7, 5, 3, 3, 2".')
for _ in range(3):
    i = int(input('Enter new rating element: '))
    flag = False
    for j in range(len(rating)):
        if rating[j] < i:
            rating.insert(j, i)
            flag = True
            break
    if not flag:
        rating.append(i)
print(f'New rating list is:')
print(*rating)

i = 1
goods = []
n = int(input('Сколько товаров Вы хотете ввести: '))
for _ in range(n):
    name = input('Введите название товара: ')
    price = int(input('Введите цену: '))
    quantity = int(input('Введите количество: '))
    measure = input('Введите единицы измерения: ')
    goods.append((i, {'Название': name, 'Цена': price, 'Количество': quantity, 'Ед.': measure}))
    i += 1
print(goods)
goods_dict = {'Название': [], 'Цена': [], 'Количество': [], 'Ед.': []}
for good in goods:
    goods_dict['Название'].append(good[1]['Название'])
    goods_dict['Цена'].append(good[1]['Цена'])
    goods_dict['Количество'].append(good[1]['Количество'])
    if good[1]['Ед.'] not in goods_dict['Ед.']:
        goods_dict['Ед.'].append(good[1]['Ед.'])
print(goods_dict)
