endColor = '\033[0m'
colors = {'orange': '\033[38;2;201;100;59m',
          'white': '\033[38;2;0;0;0m',
          'black': '\033[38;2;256;256;256m'
          }
bgColors = {
    'orange': '\033[48;2;201;100;59m',
    'black': '\033[48;2;0;0;0m',
    'white': '\033[48;2;256;256;256m'
}

styles = {
    1: '\033[1m',
    2: '\033[2m',
    3: '\033[3m',
    4: '\033[4m',
    5: '\033[5m',
    6: '\033[6m',
    7: '\033[7m',
}


def drowColor(text, txColor='white', style='0', bgColor='black'):
    newText = styles[2] + colors[txColor] + bgColors[bgColor] + text + endColor
    return newText


a = drowColor('Hello', 'orange')
print(a)
input()
