with open('task_3.txt', 'r', encoding='utf-8') as f:
    names = []
    aver_income = 0
    num = 0
    for line in f:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        aver_income += income
    aver_income /= num
print(*names)
print(aver_income)
