import os
import re
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


guests = set()
relationships = {}

r = re.compile('([a-zA-Z]+) would (gain|lose) (\d+) happiness units by sitting next to ([a-zA-Z]+)')
with open(input_filename, 'r') as f:
    for line in f:
        guest1, gain_or_lose, happiness, guest2 = r.match(line.strip()).groups()
        happiness = int(happiness)
        if gain_or_lose == 'lose':
            happiness = -happiness
        guests.add(guest1)
        guests.add(guest2)
        relationships[(guest1, guest2)] = happiness

guests = sorted(list(guests))
max_happiness = None


def get_total_happiness(guest_list):
    total_happiness = 0
    for idx, guest in enumerate(guest_list):
        if idx == 0:
            total_happiness += relationships[(guest_list[-1], guest)]
            total_happiness += relationships[(guest, guest_list[-1])]
        else:
            total_happiness += relationships[(guest_list[idx - 1], guest)]
            total_happiness += relationships[(guest, guest_list[idx - 1])]
    return total_happiness


def get_best_seating(so_far, max_happiness=None):
    if len(so_far) == len(guests):
        total_happiness = get_total_happiness(so_far)
        if max_happiness is None or total_happiness > max_happiness:
            max_happiness = total_happiness
        return max_happiness
    so_far_set = set(so_far)
    for next_guest in guests:
        if next_guest in so_far_set:
            continue
        max_happiness = get_best_seating(so_far + [next_guest], max_happiness)
    return max_happiness


print get_best_seating([guests[0]])


for guest in guests:
    relationships[(guest, 'Cucu')] = 0
    relationships[('Cucu', guest)] = 0
guests += ['Cucu']

print get_best_seating([guests[0]])
