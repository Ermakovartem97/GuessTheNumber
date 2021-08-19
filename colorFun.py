import os

endColor = '\033[0;0m'

startColor = '\033[38;2;'
startBgColor = '\033[48;2;'
colors = {
    '0': '0m',
    'menu': '148;121;77m',
    'green': '177;189;161m',
    'red': '251;115;97m',
    'yellow': '242;222;137m',
    'orange': '201;100;59m',
    'white': '255;255;255m',
    'black': '0;0;0m'
}

styles = {
    '0': '\033[0m',
    '1': '\033[1m',
    '2': '\033[4m',
    '3': '\033[7m'
}


def drawColor(text, txColor='0', bgColor='0', style='0'):
    '''

    Форматирует текст

    :param text: Текст
    :param txColor: Цвет текста ищется в словаре colors
    :param bgColor: Цвет фона ищется в словаре colors
    :param style: Стиль текста ищестя в словаре styles
    :return: Возвращает отформотированный текст
    '''
    os.system('')
    try:
        newText = styles[str(style).lower()] + startBgColor + colors[str(bgColor).lower()] + startColor + colors[str(txColor).lower()] + str(text) + endColor
    except:
        print('Неверное значение одного или нескольких аргументов')
        newText = text


    return newText

