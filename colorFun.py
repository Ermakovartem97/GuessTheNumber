endColor = '\033[0;0m'
colors = {'orange': '208',
          'white': '255'
          }


def drowColor(text, txColor='white', style='0', bgColor = 1):
    print(text)
    print(txColor)
    print(style)
    print(bgColor)
    if bgColor:
        newText = '\033[' + '38' + ';' + style + ';' + colors[txColor] + text + endColor
    else:
        newText = '\033[' + '48' + ';' + style + ';' + colors[txColor] + text + endColor
    print(newText)
    return newText

drowColor('')
