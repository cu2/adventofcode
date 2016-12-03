import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


TOTAL_VOLUME = 150


def to_bits(value, padding):
    bits = []
    for b in xrange(padding - 1, -1, -1):
        bits.append(1 if value & 2**b else 0)
    return bits


containers = []
with open(input_filename, 'r') as f:
    for line in f:
        containers.append(int(line))
N = len(containers)

min_cointainer_count = None
combination_count = 0
for combination in xrange(2**N):
    bits = to_bits(combination, N)
    if sum([cnt*vol for cnt, vol in zip(bits, containers)]) == TOTAL_VOLUME:
        combination_count += 1
        if min_cointainer_count is None or sum(bits) < min_cointainer_count:
            min_cointainer_count = sum(bits)
print combination_count

combination_count = 0
for combination in xrange(2**N):
    bits = to_bits(combination, N)
    if sum(bits) != min_cointainer_count:
        continue
    if sum([cnt*vol for cnt, vol in zip(bits, containers)]) == TOTAL_VOLUME:
        combination_count += 1
print combination_count
