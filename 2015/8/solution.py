import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


NORMAL = 0
ESCAPED = 1
ESCAPED_HEXA_1 = 2
ESCAPED_HEXA_2 = 3
HEXA_CODES = '0123456789abcdef'
def decode_string(input_string):
    output_chars = []
    state = NORMAL
    hexa_char = ''
    for input_char in input_string:
        if state == NORMAL:
            if input_char == '\\':
                state = ESCAPED
            else:
                output_chars.append(input_char)
        elif state == ESCAPED:
            if input_char in {'\\', '"'}:
                state = NORMAL
                output_chars.append(input_char)
            elif input_char == 'x':
                state = ESCAPED_HEXA_1
            else:
                raise Exception
        elif state == ESCAPED_HEXA_1:
            if input_char in HEXA_CODES:
                state = ESCAPED_HEXA_2
                hexa_char = input_char
            else:
                raise Exception
        elif state == ESCAPED_HEXA_2:
            if input_char in HEXA_CODES:
                state = NORMAL
                hexa_char += input_char
                output_chars.append(chr(int(hexa_char, 16)))
            else:
                raise Exception
        else:
            raise Exception
    return ''.join(output_chars)


def encode_string(input_string):
    output_chars = []
    for input_char in input_string:
        if input_char in {'\\', '\"'}:
            output_chars.append('\\')
        output_chars.append(input_char)
    return '"%s"' % ''.join(output_chars)


code_count = 0
mem_count = 0
encoded_count = 0

with open(input_filename, 'r') as f:
    for line in f:
        code = line.strip()
        decoded = decode_string(code[1:-1])
        encoded = encode_string(code)
        code_count += len(code)
        mem_count += len(decoded)
        encoded_count += len(encoded)

print code_count - mem_count
print encoded_count - code_count
