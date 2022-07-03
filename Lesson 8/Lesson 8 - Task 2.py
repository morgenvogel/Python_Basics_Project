class CustomZeroDivisionError(Exception):
    pass


def get_numerator() -> int:
    return int(input("Введите числитель: "))


def get_denominator() -> int:
    value = int(input("Введите знаменатель: "))

    if value == 0:
        raise CustomZeroDivisionError

    return value


while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Результат: {numerator / denominator}")
    except CustomZeroDivisionError:
        print("Вы ввели ноль в качестве знаменателя. На ноль делить нельзя!")
    except KeyboardInterrupt:
        break
