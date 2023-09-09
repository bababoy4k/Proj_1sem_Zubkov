def error():
    main(input('Вы ввели неправильное значение, пожалуйста, введите трёхзначное число: '))


def main(number):
    if len(number) == 3 and number.isdigit():
        print(f'Последняя цифра числа: {str(number)[2]}',
              f'Средняя цифра числа: {str(number)[1]}')
    else:
        error()


main((input('Введите трёхзначное число: ')))