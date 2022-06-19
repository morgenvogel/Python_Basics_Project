with open('task_1.txt', 'r', encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        number_of_words = len(value.split())
        print(f'Строка {index} содержит {number_of_words} слов.')
