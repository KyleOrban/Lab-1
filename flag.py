def green(i):
    return "\u001b[42m  " * i


def red(i):
    return "\u001b[41m  " * i


def clear():
    return "\u001b[m"


print(green(19),
      clear())

print(green(7),
      red(2),
      green(9),
      clear())

print(green(6),
      red(4),
      green(8),
      clear())

print(green(5),
      red(6),
      green(7),
      clear())

print(green(6),
      red(4),
      green(8),
      clear())

print(green(7),
      red(2),
      green(9),
      clear())


print(green(19),
      clear())