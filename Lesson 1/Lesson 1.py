#Lesson_1

a = 'Привет,'
b = 'пользователь!'
print(a, b)
number1 = int(input('Введите число: '))
number2 = int(input('Введите следующее число: '))
print(f'Вы ввели числа {number1} и {number2}.')
word = input('Введите слово: ')
print(f'{word} - это прикольно!')

sec = int(input("Введите количество секунд: "))
print(f"{sec // 3600:.0f}:{(sec // 60) % 60:.0f}:{sec % 60:.0f}")

n = input("Введите число: ")
print(int(n) + int(f"{n}{n}") + int(f"{n}{n}{n}"))

num = int(input('Введите целое положительное число: '))
max_digit = num % 10
while num:
    a = num % 10
    if a > max_digit:
        max_digit = a
        if max_digit == 9:
            break
    num = num // 10
print(f'Наибольшая цифра в {num} равна {max_digit}')

income = int(input('Введите выручку: '))
expense = int(input('Введите издержки: '))
net_income = income - expense
if net_income > 0:
    print('Фирма работает с прибылью.')
    print(f'Рентабельность выручки: {net_income / income: .2f}')
    people = int(input('Введите численность сотрудников: '))
    print(f'Прибыль фирмы в расчёте на одного сотрудника: {net_income / people: .2f}')
elif net_income < 0:
    print('Фирма работает с убытком.')

a = int(input('Сколько километров спортсмен пробежал в первый день: '))
b = int(input('Срок достижения какого результата нужно узнать: '))
days = 1
while a < b:
    a = a * 1.1
    days = days + 1
print(f'Спортсмен достиг результата на {days}-й день.')