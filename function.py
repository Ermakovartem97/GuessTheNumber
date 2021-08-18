def EnterNumber(text):
    '''
    Функция ввода и проверки, что на ввод подали целое число

    :param text: Текст который необходимо проверить
    :return: Введенное пользователем число
    '''
    isNumber = False
    userNumber = input(text)

    while not isNumber:
        if not userNumber.isdigit():
            userNumber = input('Пожалуйста введите челое число: ')
        else:
            isNumber = True
    return int(userNumber)


def levelOption(level):
    option = {
        1: [1, 10],
        2: [1, 100],
        3: [1, 1000]
    }
    return option[level]
