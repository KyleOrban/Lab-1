with open('sequence.txt') as file:
    numbers = list()
    for element in file:
        numbers.append(float(element))

numnum1 = []
numnum2 = []
for i in range(0, 125):
    numnum1.append(abs(numbers[i]))

for i in range(125, 250):
    numnum2.append(abs(numbers[i]))

num1 = 0
num2 = 0

for i in numnum1:
    num1+=i
for i in numnum2:
    num2+=i
num1 = round(num1)
num2 = round(num2)

sumnum = num1+num2

num1perc = int(round(num1 / sumnum * 100))
num2perc = int(round(num2 / sumnum * 100))


def green(i):
    return "\u001b[42m  " * i


def red(i):
    return "\u001b[41m  " * i


def clear():
    return "\u001b[m"


print(green(num1perc), num1perc, clear(), "первые 125")
print(red(num2perc), num2perc, clear(), "вторые 125")
