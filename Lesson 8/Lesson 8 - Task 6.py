from datetime import datetime


class WareHouse:
    contents = {}

    @staticmethod
    def get(name, quantity, where_to):
        exists = False
        if name in WareHouse.contents.keys():
            exists = True
            if WareHouse.contents[name] >= quantity:
                WareHouse.contents[name] -= quantity
                print(f'\n{quantity} units of {name} have been moved from warehouse to {where_to}\n')
                save_history(f'Moved {quantity} units of {name} from warehouse to {where_to}')
                if WareHouse.contents[name] == 0:
                    WareHouse.contents.pop(name)
            else:
                print(f"\nWarehouse doesn't contain enough units. The available quantity of {name} is "
                      f"{WareHouse.contents[name]}\n")
        if not exists:
            print(f"\nWarehouse doesn't contain equipment named {name}\n")

    @staticmethod
    def view_contents():
        text = str(WareHouse.contents)
        text = text.replace('{', '').replace('}', '\n').replace("'", '')
        print(text) if text.replace('\n', '') else print('\nThe warehouse is empty\n')


class OfficeEquipment:
    def __init__(self):
        self.name = input('Enter the name of the equipment: ')
        self.price = input("Enter equipment's price: ")

    def warehouse_put(self, quantity):
        already_there = False
        if self.name in WareHouse.contents.keys():
            WareHouse.contents[self.name] += quantity
            already_there = True
        if not already_there:
            WareHouse.contents.update({self.name: quantity})
        save_history(f'Added {quantity} units of equipment {self.name}')
        print('\nItems added\n')


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.print_spd = input('Enter the printing speed: ')


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.scan_res = input('Enter the scan resolution: ')


class Copier(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.copies_per_min = input("Enter the copy speed in copies per minute: ")


def save_history(message):
    current_time = datetime.now()
    text = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')


if __name__ == '__main__':
    stop = False

    while not stop:
        command = input('1 - view the warehouse contents\n'
                        '2 - add equipment to the warehouse\n'
                        '3 - distribute the equipment from the warehouse to a specified place\n'
                        '4 - exit the program\n'
                        '\nChoose the option: ')
        if command == '1':
            WareHouse.view_contents()
        elif command == '2':
            try:
                to_add = input('1 - add a printer\n'
                               '2 - add a scanner\n'
                               '3 - add a copier\n'
                               '\nChoose what you want to add: ')
                if to_add == '1':
                    printer = Printer()
                    eq_quantity = int(input(f'How many of {printer.name} would you like to add? '))
                    printer.warehouse_put(eq_quantity)
                elif to_add == '2':
                    scanner = Scanner()
                    eq_quantity = int(input(f'How many of {scanner.name} would you like to add? '))
                    scanner.warehouse_put(eq_quantity)
                elif to_add == '3':
                    copier = Copier()
                    eq_quantity = int(input(f'How many of {copier.name} would you like to add? '))
                    copier.warehouse_put(eq_quantity)
                else:
                    print('\nUnexpected command')
                    break
            except ValueError:
                print('\nQuantity should be a number\n')
        elif command == '3':
            eq_name = input('Enter the name of the equipment you would like to distribute: ')
            if eq_name in WareHouse.contents.keys():
                eq_quantity = int(input('Enter the quantity: '))
                eq_where_to = input('Enter the department for the distribution: ')
                WareHouse.get(eq_name, eq_quantity, eq_where_to)
            else:
                print(f"\nWarehouse doesn't contain equipment named {eq_name}\n")
        elif command == '4':
            stop = True
        else:
            print('\nUnexpected command')
