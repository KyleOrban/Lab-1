import time
def black(i):
    return "\x1b[40;1m  " * i


def grey(i):
    return "\x1b[47;1m  " * i


def clear():
    return "\u001b[m"


while True:
    for i in range(16):
        print(black(75), grey(32), clear())

    for i in range(16):
        print(black(17), grey(41), black(16), grey(32), clear())

    for i in range(16):
        print(black(17), grey(14), black(43), grey(32), clear())

    for i in range(17):
        print(black(17), grey(14), black(17), grey(58), clear())

    for i in range(17):
        print(black(17), grey(14), black(76), clear())

    time.sleep(1)