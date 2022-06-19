with open('task_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите текст и нажмите Enter, введите пустую строку для записи файла: ')
        if not line:
            break
        print(line, file=f)
