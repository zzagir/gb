class MyTypeError(Exception):
    pass


def my_func():
    try:
        x = int(input("Введите число: "))
        y = int(input("Введите делитель: "))
        if y == 0:
            raise MyTypeError('На ноль делить нельзя!')

        else:
            result = x / y
            return result

    except ValueError:
        return "Введите число!"
    except MyTypeError as err:
        return err


print(my_func())
