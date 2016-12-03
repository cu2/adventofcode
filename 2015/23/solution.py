import copy
import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def parse_code(code):
    instruction, raw_arguments = code.split(' ', 1)
    arguments = [raw_argument.strip() for raw_argument in raw_arguments.split(',')]
    return {
        'instruction': instruction,
        'arguments': arguments,
    }


def run_program(program, initial_registers, verbose=False):
    registers = copy.deepcopy(initial_registers)
    while True:
        try:
            next_line = program[registers['ip']]
        except IndexError:
            break  # end of program
        if verbose:
            print '[%d] %s %s a=%d b=%d' % (
                registers['ip'],
                next_line['instruction'],
                next_line['arguments'],
                registers['a'],
                registers['b'],
            )
        if next_line['instruction'] == 'hlf':
            registers[next_line['arguments'][0]] /= 2
            next_ip = registers['ip'] + 1
        elif next_line['instruction'] == 'tpl':
            registers[next_line['arguments'][0]] *= 3
            next_ip = registers['ip'] + 1
        elif next_line['instruction'] == 'inc':
            registers[next_line['arguments'][0]] += 1
            next_ip = registers['ip'] + 1
        elif next_line['instruction'] == 'jmp':
            next_ip = registers['ip'] + int(next_line['arguments'][0])
        elif next_line['instruction'] == 'jie':
            if registers[next_line['arguments'][0]] % 2 == 0:
                next_ip = registers['ip'] + int(next_line['arguments'][1])
            else:
                next_ip = registers['ip'] + 1
        elif next_line['instruction'] == 'jio':
            if registers[next_line['arguments'][0]] == 1:
                next_ip = registers['ip'] + int(next_line['arguments'][1])
            else:
                next_ip = registers['ip'] + 1
        else:
            raise Exception('Unknown instruction: %s at IP %d' % (next_line['instruction'], registers['ip']))
        registers['ip'] = next_ip
    return registers


program = []
with open(input_filename, 'r') as f:
    for line in f:
        program.append(parse_code(line.strip()))

registers = run_program(program, {
    'a': 0,
    'b': 0,
    'ip': 0,
})
print registers['b']

registers = run_program(program, {
    'a': 1,
    'b': 0,
    'ip': 0,
})
print registers['b']
