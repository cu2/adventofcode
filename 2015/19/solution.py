import random


def parse_molecule(raw_molecule):
    molecule = []
    particle = ''
    for ch in raw_molecule:
        if ch == 'e' or ch == ch.upper():
            if particle:
                molecule.append(particle)
            particle = ch
        else:
            particle += ch
    if particle:
        molecule.append(particle)
    return molecule


def load_input():
    import os
    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    periodic_table = set()
    replacements = {}
    medicine_molecule = []
    input_phase = 0
    with open(input_filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                input_phase = 1
            else:
                if input_phase == 1:
                    medicine_molecule = parse_molecule(line)
                    for particle in medicine_molecule:
                        periodic_table.add(particle)
                else:
                    raw_from, raw_to = line.split(' => ')
                    from_piece = parse_molecule(raw_from)[0]
                    to_pieces = parse_molecule(raw_to)
                    if from_piece not in replacements:
                        replacements[from_piece] = [to_pieces]
                    else:
                        replacements[from_piece].append(to_pieces)
                    periodic_table.add(from_piece)
                    for particle in to_pieces:
                        periodic_table.add(particle)
    return (replacements, medicine_molecule, sorted(list(periodic_table)))


def get_spectrum(molecule, periodic_table):
    spectrum = []
    for particle in periodic_table:
        spectrum.append(molecule.count(particle))
    return spectrum


def fits_spectrum(molecule, spectrum, periodic_table, important_particles):
    # return True
    molecule_spectrum = get_spectrum(molecule, periodic_table)
    for particle, mol_count, spec_count in zip(periodic_table, molecule_spectrum, spectrum):
        if particle in important_particles:
            # print particle, mol_count, spec_count
            if mol_count > spec_count:
                return False
    return True


def generate_all_replacements(molecule, replacements, sample=False):
    new_molecules = set()
    full_pop = list(enumerate(molecule))
    if sample:
        x = random.sample(full_pop, 1 + len(full_pop) / 10)
    else:
        x = full_pop
    for idx, particle in full_pop:
        if particle in replacements:
            for to_pieces in replacements[particle]:
                new_molecule = molecule[:idx] + to_pieces + molecule[idx+1:]
                new_molecules.add(''.join(new_molecule))
    return [parse_molecule(raw_molecule) for raw_molecule in new_molecules]


# def get_score(molecule_spectrum, medicine_molecule_spectrum):
#     return sum([(a-b)**2 for a, b in zip(molecule_spectrum, medicine_molecule_spectrum)])


def get_score(molecule, medicine_molecule):
    return sum([(0 if a == b else 1) for a, b in zip(molecule, medicine_molecule)]) + abs(len(molecule) - len(medicine_molecule))


replacements, medicine_molecule, periodic_table = load_input()
medicine_molecule_spectrum = get_spectrum(medicine_molecule, periodic_table)

delta_particles = {particle: set() for particle in periodic_table}
for from_piece, to_pieces in replacements.iteritems():
    for to_piece in to_pieces:
        for p in set([from_piece] + to_piece):
            delta = to_piece.count(p) - [from_piece].count(p)
            delta_particles[p].add(delta)

plus_particles = set()  # cannot decrease
zero_particles = set()  # cannot increase
minus_particles = set()  # can do both
for particle, deltas in delta_particles.iteritems():
    print particle, sorted(list(deltas))
    plus, minus = False, False
    for delta in deltas:
        if delta < 0:
            minus = True
        if delta > 0:
            plus = True
    if plus:
        if minus:
            zero_particles.add(particle)
        else:
            plus_particles.add(particle)
    else:
        if minus:
            minus_particles.add(particle)
        else:
            zero_particles.add(particle)
# exit()

print len(generate_all_replacements(medicine_molecule, replacements))

old_molecules = [['e']]
new_molecule = []
number_of_steps = 0
still_searching = True
while still_searching:
    number_of_steps += 1
    new_molecules = set()
    possibility_count = 0
    for old_molecule in old_molecules:
        possible_new_molecules = generate_all_replacements(old_molecule, replacements, sample=True)
        possibility_count += len(possible_new_molecules)
        possible_new_molecules_with_score = []
        for new_molecule in possible_new_molecules:
            new_molecule_spectrum = get_spectrum(new_molecule, periodic_table)
            # new_molecule_score = get_score(new_molecule_spectrum, medicine_molecule_spectrum)
            new_molecule_score = get_score(new_molecule, medicine_molecule)
            possible_new_molecules_with_score.append((new_molecule_score, new_molecule))
        possible_new_molecules_with_score.sort(key=lambda item: item[0])
        for new_molecule_score, new_molecule in possible_new_molecules_with_score[:10]:
            # print new_molecule
            # if len(new_molecule) <= len(medicine_molecule) and fits_spectrum(new_molecule, medicine_molecule_spectrum, periodic_table, plus_particles):
            new_molecules.add(''.join(new_molecule))
            if new_molecule == medicine_molecule:
                print new_molecule
                still_searching = False
    ###
    possible_new_molecules_with_score = []
    for new_molecule in [parse_molecule(raw_molecule) for raw_molecule in new_molecules]:
        new_molecule_spectrum = get_spectrum(new_molecule, periodic_table)
        # new_molecule_score = get_score(new_molecule_spectrum, medicine_molecule_spectrum)
        new_molecule_score = get_score(new_molecule, medicine_molecule)
        possible_new_molecules_with_score.append((new_molecule_score, new_molecule))
    possible_new_molecules_with_score.sort(key=lambda item: item[0])
    old_molecules = [new_molecule for new_molecule_score, new_molecule in possible_new_molecules_with_score[:100]]
    ###
    print number_of_steps, len(new_molecules), possibility_count, len(new_molecule), len(medicine_molecule), possible_new_molecules_with_score[0][0]
    print ''.join(possible_new_molecules_with_score[0][1][:10])
    if possibility_count == 0:
        break
print number_of_steps

# print replacements
# print medicine_molecule
# print get_spectrum(medicine_molecule)

# That's not the right answer; your answer is too high.
# (You guessed 279.)





### OLD CODE
exit()


def generate_all_replacements(input_molecule, replacements):
    results = set()
    for from_piece, to_piece in replacements:
        pos = None
        for _ in xrange(input_molecule.count(from_piece)):
            pos = input_molecule.find(from_piece, 0 if pos is None else pos + 1)
            results.add(''.join([input_molecule[:pos], to_piece, input_molecule[pos + len(from_piece):]]))
    return results


def generate_all_reverse_replacements(input_molecule, replacements):
    results = set()
    for from_piece, to_piece in replacements:
        pos = None
        for _ in xrange(input_molecule.count(to_piece)):
            pos = input_molecule.find(to_piece, 0 if pos is None else pos + 1)
            results.add(''.join([input_molecule[:pos], from_piece, input_molecule[pos + len(to_piece):]]))
    return results


replacements = []
input_molecule = ''
input_phase = 0
with open(input_filename, 'r') as f:
    for line in f:
        line = line.strip()
        if line == '':
            input_phase = 1
        else:
            if input_phase == 1:
                input_molecule = line
            else:
                replacements.append(line.split(' => '))

print len(generate_all_replacements(input_molecule, replacements))

old_molecules = ['e']
number_of_steps = 0
while True:
    number_of_steps += 1
    new_molecules = set()
    for old_molecule in old_molecules:
        for new_molecule in generate_all_replacements(old_molecule, replacements):
            if len(new_molecule) <= len(input_molecule):
                new_molecules.add(new_molecule)
                if len(new_molecule) == len(input_molecule):
                    print '!!!'
    old_molecules = new_molecules
    print number_of_steps, len(new_molecules), len(new_molecule), len(input_molecule)
    if input_molecule in new_molecules:
        break
print number_of_steps

# print len(generate_all_reverse_replacements(input_molecule, replacements))

# old_molecules = [input_molecule]
# number_of_steps = 0
# while True:
#     number_of_steps += 1
#     new_molecules = set()
#     for old_molecule in old_molecules:
#         for new_molecule in generate_all_reverse_replacements(old_molecule, replacements):
#             if new_molecule == 'e':
#                 break
#             new_molecules.add(new_molecule)
#     old_molecules = new_molecules
#     print number_of_steps, len(new_molecules), len(new_molecule)
# print number_of_steps
