x_axis = [str(i) + '  ' for i in range(10)]
y_axis = [str(i * 2 + 3) for i in range(0, 100, 10)]

for current_string in range(9, -1, -1):
    if len(y_axis[current_string]) == 2:
        print(y_axis[current_string] + ' \t' * (current_string + 2) + "!!")
    elif len(y_axis[current_string]) == 1:
        print(y_axis[current_string] + ' \t' * (current_string + 2) + "!!")
    else:
        print(y_axis[current_string] + ' \t' * (current_string + 1) + "!!")
print('\n', ' ' * 6, *x_axis)