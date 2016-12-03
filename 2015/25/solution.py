def load_input():
    import os
    import re
    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    with open(input_filename, 'r') as f:
        input_text = f.read().strip()
    raw_row, raw_column = re.match('To continue, please consult the code grid in the manual\.  Enter the code at row (\d+), column (\d+)\.', input_text).groups()
    return int(raw_row), int(raw_column)


def get_layer_number(row, column):
    return row + column


def get_serial_number(row, column):
    layer_number = get_layer_number(row, column)
    return (layer_number - 2) * (layer_number - 1) / 2 + column


row, column = load_input()

serial_number = get_serial_number(row, column)

for n in xrange(serial_number):
    if n == 0:
        code = 20151125
    else:
        code = (code * 252533) % 33554393

print code
