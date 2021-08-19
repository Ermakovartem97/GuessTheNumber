from random import randint
from colorFun import drawColor
from function import EnterNumber, levelOption, textDeclination, stageFun
import os

endGame = True

while endGame:

    os.system("cls")  # Очистка консоли
    # Главное меню
    endGame = EnterNumber(drawColor('Главное меню', 'Menu') + '\n1 - Новая игра \n0 - Выход\n')
    os.system("cls")  # Очистка консоли
    # Выход из приложения (main loop)
    if endGame == 0:
        print('До скорой встречи!')
        break

    elif endGame == 1:  # Если выбрана "Новая игра"

        alert = ''

        # Выбор уровня
        level = 0
        while level < 1 or level > 3:
            print(alert, end='')
            level = EnterNumber(drawColor('Выберите уровень', 'menu') +
                                '\n1 - ' + drawColor('Легкий', 'green') +
                                '\n2 - ' + drawColor('Средний', 'yellow') +
                                '\n3 - ' + drawColor('Сложный', 'red') + '\n')
            os.system("cls")  # Очистка консоли
            alert = drawColor('Выберите уровень из предоставленных\n', 'red')

        # Начальные значения для выбранного уровня
        option = levelOption(level)
        minNum = option[0]
        maxNum = option[1]
        number = randint(minNum, maxNum)  # Компьютер загадывает число
        win = False  # Критерий остановки цикала (выйграл ли пользователь)
        os.system("cls")  # Очистка консоли
        alert = ''  # Сообщение в начале каждого цикла
        countTry = 0
        score = 1000
        preAlert = '' # Сообщение перед вниманием добавляется каждый шаг новое
        timePreAlert = ''
        timeOutAlert = 0

        # Цикл игры
        while not win:

            os.system("cls")
            print(number)
            print(preAlert, end='')
            print(alert, end='')
            alert = ''
            stage = 0  # Стадия подсказок

            if timeOutAlert == 1:
                timeOutAlert = 0
                preAlert += timePreAlert

            # Функция для ввода и проверки числа.
            userNumber = EnterNumber(f'Угадай число от {minNum} до {maxNum}: ')
            countTry += 1

            stage = stageFun(countTry)

            # Если число угадано
            if userNumber == number:
                os.system("cls")  # Очистка консоли
                print('Ура вы выйграли!')
                print(f'Вы отгадали число за ' + drawColor(countTry, 'orange') + ' ' + textDeclination(countTry, 'ход'))
                input('\nНажмите Enter, чтобы продолжить')

                win = True  # Конец игры

            # Если число не попадает в диапазон выводится соответствующее предложение.
            if userNumber > maxNum or userNumber < minNum:
                alert += drawColor('Мне кажется число немного не попадает в диапазон\n', 'orange')

            # Если игрок не угадал число
            if alert == '':
                alert += f'Нет, это не {userNumber}\n'

            if stage == 1:
                alert += 'Не сдавайтесь у вас все получится!\n'
            elif stage == 2:
                if number % 2 == 0:
                    evenNum = 'Четное'
                else:
                    evenNum = 'Нечетное'
                alert += 'Я тайно узнал, что загаданное число ' + drawColor(evenNum, 'orange') + '\n'
                timeOutAlert = 1
                timePreAlert += 'Загаданное число ' + drawColor(evenNum, 'orange') + '\n'

input('Нажмите Enter')  # Задержка в консоли
