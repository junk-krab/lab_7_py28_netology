class Custom_Exeption(Exception):
   pass

input_list = input('Введите оператор и два числа: ').split(' ')

try:
    assert input_list[0] in ['+', '-', '*', '/']
    num_1 = int(input_list[1])
    num_2 = int(input_list[2])
    if input_list[0] == '/' and num_2 == 0:
        raise ZeroDivisionError
    if len(input_list) != 3:
        raise Custom_Exeption
except AssertionError:
    print('Не выбрано арифметическое действие!')
except ValueError:
    print('Вы ввели не число!')
except ZeroDivisionError:
    print('Нельзя делить на 0')
except Exception as exc_type:
    print(f'Какая то другая ошибка. {exc_type}')
except Custom_Exeption:
    print('Неверное количество чисел')
else:
    if input_list[0] == '+':
        print(f'Результат сложения: {num_1 + num_2}')
    elif input_list[0] == '-':
        print(f'Результат вычитания: {num_1 - num_2}')
    elif input_list[0] == '*':
        print(f'Результат умножения: {num_1 * num_2}')
    elif input_list[0] == '/':
        print(f'Результат деления: {num_1 / num_2}')