def div(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print('Division by zero is forbidden!')
    except ValueError:
        print('You should enter integers!')


print(div(input('Input first digital value: '), input('Input second digital value: ')))


def print_data(**kwargs):
    return ' '.join(kwargs.values())


print(print_data(name=input('Enter your name: '), surname=input('Enter your surname: '), birth_year=input('Enter your year of birth: '), city=input('Enter your city: '), email=input('Enter your email: '), phone=input('Input your phone number: ')))


def my_func(a, b, c):
    try:
        return sum((a, b, c)) - min(a, b, c)
    except TypeError:
        return 'Enter only numbers!'


print(my_func(10, 10, 2))


def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает только с действительными x и целыми y!')
        return
    if x <= 0 or y >= 0:
        print('Программа работает только с положительными x и отрицательными y!')
        return
    return x ** y


print(round(my_func(2, -2), 10))


def pow_negative(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает тольок с действительными x и целыми y!')
        return
    if x <= 0 or y >= 0:
        print('Программа работает только с положительными x и отрицательными y!')
        return
    result = 1
    for _ in range(abs(y)):
        result /= x
    return result


print(round(pow_negative(input('Введите действительный положительный x: '), input('Введите целый отрицательный y: ')), 10))


def my_func():
    s = 0
    in_list = input('Введите числа через пробел или Q для выхода: ').upper().split()
    for i in in_list:
        if i == 'Q':
            return s, True
        try:
            s += int(i)
        except ValueError:
            pass
    return s, False


res = 0
while True:
    a, b = my_func()
    res += a
    print(res)
    if b:
        break


def int_func(word):
    return word[0].upper() + word[1:].lower()


s = input().split()
for i, word in enumerate(s):
    if not word.isascii() or not word.isalpha or not word.islower():
        print('Error!!!')
    else:
        s[i] = int_func(word)


print(' '.join(s))
