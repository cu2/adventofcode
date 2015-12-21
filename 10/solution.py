import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def look_and_say(input_sequence):
    current_digit = None
    digit_count = 0
    output_sequence = []
    for input_digit in input_sequence:
        if input_digit != current_digit:
            if digit_count:
                output_sequence.append(str(digit_count))
                output_sequence.append(current_digit)
            current_digit = input_digit
            digit_count = 0
        digit_count += 1
    if digit_count:
        output_sequence.append(str(digit_count))
        output_sequence.append(current_digit)
    return ''.join(output_sequence)


with open(input_filename, 'r') as f:
    puzzle_sequence = f.read()

for _ in xrange(40):
    puzzle_sequence = look_and_say(puzzle_sequence)

print len(puzzle_sequence)

for _ in xrange(10):
    puzzle_sequence = look_and_say(puzzle_sequence)

print len(puzzle_sequence)
