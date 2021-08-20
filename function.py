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
            userNumber = input('Пожалуйста введите челое положительное число: ')
        else:
            isNumber = True
    return int(userNumber)


def levelOption(level):
    '''

    Выбор диапазона чисел для выбранного уровня

    :param level: Выбранный уровень
    :return: Диапазон чисел
    '''
    option = {
        1: [1, 10],
        2: [1, 100],
        3: [1, 1000]
    }
    return option[level]


def textDeclination(num, text):
    '''
    Правильное склонение слов

    :param num: Число для которого склоняется слово
    :param text: Какое слово склонять
    :return: Правильное слово для данного числа
    '''

    userTry = {
        1: 'ход',
        2: 'хода',
        3: 'хода',
        4: 'хода',
        5: 'ходов',
        6: 'ходов',
        7: 'ходов',
        8: 'ходов',
        9: 'ходов',
    }
    if text == 'ход':
        userDict = userTry
    ans = num % 10
    return userDict[ans]


def stageFun(countryTry):
    stageArr = [[1, 2], [3], [4, 5], [6]]
    userStage = 4
    for i in range(len(stageArr)):
        if countryTry in stageArr[i]:
            userStage = i + 1
    return userStage

def coldHot(number, userNumber):
    diff = abs(number - userNumber)
    if diff < 2:
        ans = 'Все вокруг плавится'
    elif diff < 5:
        ans = 'Горяченно'
    elif diff < 10:
        ans = 'Впринципе тепло'
    elif diff < 15:
        ans = 'Комнатная температура'
    elif diff < 20:
        ans = 'Прохладненько'
    elif diff < 25:
        ans = 'Дайте мне шапку и горячий какао'
    else:
        ans = 'Ледяной ветер'

    return ans