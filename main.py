def dodavannya(x, y):
    return x + y


def viddilennya(x, y):
    if y == 0:
        print("Дільник не може бути нулем!")
        return None
    else:
        return x / y


def mnozhennya(x, y):
    return x * y


def vidnimannya(x, y):
    return x - y


while True:
    try:
        x = float(input("Введіть перше число: "))
        y = float(input("Введіть друге число: "))
        operation = input("Введіть операцію (+, -, *, /): ")

        if operation == '+':
            print("Результат:", dodavannya(x, y))
        elif operation == '-':
            print("Результат:", vidnimannya(x, y))
        elif operation == '*':
            print("Результат:", mnozhennya(x, y))
        elif operation == '/':
            result = viddilennya(x, y)
            if result is not None:
                print("Результат:", result)
        else:
            print("Неправильна операція! Будь ласка, введіть один з символів: +, -, *, /")

        repeat = input("Бажаєте продовжити? (так/ні): ")
        if repeat.lower() != 'так':
            break
    except ValueError:
        print("Будь ласка, введіть коректне число!")