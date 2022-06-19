from json import dump

with open('tast_7.json', 'w', encoding='utf-8') as write_file:
    with open('task_7.txt', encoding='utf-8') as read_file:
        dictionary = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in read_file}
        average_profit_list = []
        for n in dictionary.values():
            if n > 0:
                average_profit_list.append(n)
        dump([dictionary, {'average_profit': sum(average_profit_list) / len(average_profit_list)}], write_file,
             ensure_ascii=False, indent=4)
