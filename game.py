from random import randint
from function import EnterNumber, levelOption
import os

# Глобальные переменные

endGame = True

while endGame:

    # Очистка консоли
    os.system("cls")

    endGame = EnterNumber('Главное меню\n1 - Новая игра \n0 - Выход\n')

    os.system("cls")

    if endGame == 0:
        print('До скорой встречи!')
        break

    elif endGame == 1:
        # Выбор уровня
        level = EnterNumber('Выберите уровень\n1 - Легкий\n2 - Средний\n3 - Сложный\n')

        # Начальные значения для выбранного уровня
        option = levelOption(level)
        minNum = option[0]
        maxNum = option[1]

        # Компьютер загадывает число
        number = randint(minNum, maxNum)

        win = False

        os.system("cls")

        while not win:

            os.system("cls")
            print(number)

            # Функция для ввода и проверки числа.
            userNumber = EnterNumber(f'Угадай число от {minNum} до {maxNum}: ')

            # Если число угадано
            if userNumber == number:
                print('Ура ты выйграл!\n')
                input('Нажмите Enter, чтобы продолжить')

                # Конец игры
                win = True
input('Нажмите Enter')
