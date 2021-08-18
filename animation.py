import sys
import time
import os

from colorFun import drowColor


def load_animation():
    # animation = "|/-\\"
    text = 'Hello'
    animation = ['.', '..', '...', '']
    anicount = 0
    counttime = 0
    i = 0
    while (counttime != 100):
        time.sleep(0.35)
        sys.stdout.write("\r" + animation[anicount])
        sys.stdout.flush()

        i = (i + 1) % len(text)
        anicount = (anicount + 1) % len(animation)
        counttime = counttime + 1

    os.system("cls")


if __name__ == '__main__':
    load_animation()
