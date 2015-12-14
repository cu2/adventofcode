with open('input', 'r') as f:
    instructions = f.read()

INSTURCTION_CODE = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
}

def add_tuples(*args):
    return tuple([sum(dim) for dim in zip(*args)])


santa = (0, 0)
visited_houses = {santa}

for instruction in instructions:
    santa = add_tuples(santa, INSTURCTION_CODE[instruction])
    visited_houses.add(santa)

print len(visited_houses)


santa = robo = (0, 0)
visited_houses = {santa}

for idx, instruction in enumerate(instructions):
    if idx % 2 == 0:
        santa = add_tuples(santa, INSTURCTION_CODE[instruction])
        visited_houses.add(santa)
    else:
        robo = add_tuples(robo, INSTURCTION_CODE[instruction])
        visited_houses.add(robo)

print len(visited_houses)
