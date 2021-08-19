from random import randint

from colorFun import drawColor
from function import EnterNumber, levelOption
import os

# Глобальные переменные

endGame = True

while endGame:

    # Очистка консоли
    os.system("cls")

    #Главное меню
    endGame = EnterNumber(drawColor('Главное меню', 'Menu') + '\n1 - Новая игра \n0 - Выход\n')

    os.system("cls")

    # Выход из приложения (main loop)
    if endGame == 0:
        print('До скорой встречи!')
        break

    # Если выбрана "Новая игра"
    elif endGame == 1:
        # Выбор уровня
        level = EnterNumber(drawColor('Выберите уровень', 'menu') +
                            '\n1 - ' + drawColor('Легкий', 'green') +
                            '\n2 - ' + drawColor('Средний', 'yellow') +
                            '\n3 - ' + drawColor('Сложный', 'red') + '\n')

        # Начальные значения для выбранного уровня
        option = levelOption(level)
        minNum = option[0]
        maxNum = option[1]

        # Компьютер загадывает число
        number = randint(minNum, maxNum)

        # Критерий остановки цикала (выйграл ли пользователь)
        win = False

        os.system("cls")

        # Сообщение в начале каждого цикла
        alert = ''

        #Цикл игры
        while not win:

            os.system("cls")
            print(number)
            print(alert, end='')
            alert = ''

            # Функция для ввода и проверки числа.
            userNumber = EnterNumber(f'Угадай число от {minNum} до {maxNum}: ')

            # Если число угадано
            if userNumber == number:
                print('Ура ты выйграл!\n')
                input('Нажмите Enter, чтобы продолжить')

                # Конец игры
                win = True

            if userNumber > maxNum or userNumber < minNum:
                alert = drawColor('Мне кажется число немного не попадает в диапазон\n', 'orange')

            if alert == '':
                alert = f'Нет, это не {userNumber}\n'
input('Нажмите Enter')
