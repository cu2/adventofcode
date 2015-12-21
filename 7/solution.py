def get_value(wires, inp):
    if inp['type'] == 'value':
        return inp['value']
    return wires[inp['name']]['value']


def input_string_to_input(input_string):
    try:
        return {
            'type': 'value',
            'value': int(input_string),
        }
    except ValueError:
        pass
    return {
        'type': 'wire',
        'name': input_string,
    }


def parse_wire_input(wire_input):
    try:
        value = int(wire_input)
        return {
            'value': value,
            'gate': None,
            'inputs': [],
        }
    except ValueError:
        pass
    if ' ' not in wire_input:
        return {
            'value': None,
            'gate': 'ID',
            'inputs': [input_string_to_input(wire_input)],
        }
    if wire_input[:3] == 'NOT':
        return {
            'value': None,
            'gate': 'NOT',
            'inputs': [input_string_to_input(wire_input[4:])],
        }
    input1, gate, input2 = wire_input.split(' ')
    return {
        'value': None,
        'gate': gate,
        'inputs': [input_string_to_input(input1), input_string_to_input(input2)],
    }


def calculate_wire_value(wires, wire_name):
    wire = wires[wire_name]
    input_values = []
    for inp in wire['inputs']:
        input_value = get_value(wires, inp)
        if input_value is None:
            return None
        input_values.append(input_value)
    if wire['gate'] == 'ID':
        return input_values[0]
    if wire['gate'] == 'NOT':
        return ~ input_values[0]
    if wire['gate'] == 'AND':
        return input_values[0] & input_values[1]
    if wire['gate'] == 'OR':
        return input_values[0] | input_values[1]
    if wire['gate'] == 'LSHIFT':
        return input_values[0] << input_values[1]
    if wire['gate'] == 'RSHIFT':
        return input_values[0] >> input_values[1]
    raise Exception('Unknown gate')


def solve_wires(wires, wire_graph):
    wires_with_value = set()
    wires_without_value = set()
    for wire_name, wire in wires.iteritems():
        if wire['value'] is not None:
            wires_with_value.add(wire_name)
        else:
            wires_without_value.add(wire_name)
    while wires_without_value:
        new_wires_with_value = set()
        for wire in wires_with_value:
            if wire in wire_graph:
                for next_wire_name in wire_graph[wire]:
                    if next_wire_name in wires_with_value:
                        continue
                    value = calculate_wire_value(wires, next_wire_name)
                    print wire, next_wire_name, value
                    if value is not None:
                        wires[next_wire_name]['value'] = value
                        new_wires_with_value.add(next_wire_name)
                        if next_wire_name in wires_without_value:
                            wires_without_value.remove(next_wire_name)
        wires_with_value |= new_wires_with_value
        print len(wires_without_value)


wires = {}
wire_graph = {}
with open('input', 'r') as f:
    for line in f:
        wire_input, wire_name = line.strip().split(' -> ')
        wire = parse_wire_input(wire_input)
        wires[wire_name] = wire
        for inp in wire['inputs']:
            if inp['type'] == 'wire':
                if inp['name'] not in wire_graph:
                    wire_graph[inp['name']] = []
                wire_graph[inp['name']].append(wire_name)


solve_wires(wires, wire_graph)
print wires['a']['value']
# 16076
# 2797  # no comment...

# doesn't work:
# selected_value = wires['a']['value']
# for wire_name in wires:
#     if wire_name == 'b':
#         wires[wire_name] = {
#             'value': selected_value,
#             'gate': None,
#             'inputs': [],
#         }
#     else:
#         wires[wire_name]['value'] = None
# solve_wires(wires, wire_graph)
# print wires['a']['value']
