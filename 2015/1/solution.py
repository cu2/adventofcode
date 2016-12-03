with open('input', 'r') as f:
    instructions = f.read()

print instructions.count('(') - instructions.count(')')

floor = 0
step = 0

while True:
    if floor == -1:
        break
    floor += 1 if instructions[step] == '(' else -1
    step += 1

print step
