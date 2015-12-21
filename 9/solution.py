import os
import re
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


stars = set()
distances = {}

r = re.compile('([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)')
with open(input_filename, 'r') as f:
    for line in f:
        star1, star2, distance = r.match(line.strip()).groups()
        stars.add(star1)
        stars.add(star2)
        distances[(star1, star2)] = int(distance)
        distances[(star2, star1)] = int(distance)

stars = sorted(list(stars))

def get_shortest_route(so_far=None, min_distance=None):
    if so_far is None:
        so_far = []
    total_distance_so_far = sum([distances[(this_step, so_far[idx + 1])]  for idx, this_step in enumerate(so_far[:-1])])
    if len(so_far) == len(stars):
        if min_distance is None or total_distance_so_far < min_distance:
            min_distance = total_distance_so_far
        return min_distance
    if min_distance is not None:
        if total_distance_so_far > min_distance:
            return min_distance
    so_far_set = set(so_far)
    for next_step in stars:
        if next_step not in so_far_set:
            min_distance = get_shortest_route(so_far + [next_step], min_distance)
    return min_distance

def get_longest_route(so_far=None, max_distance=None):
    if so_far is None:
        so_far = []
    total_distance_so_far = sum([distances[(this_step, so_far[idx + 1])]  for idx, this_step in enumerate(so_far[:-1])])
    if len(so_far) == len(stars):
        if max_distance is None or total_distance_so_far > max_distance:
            max_distance = total_distance_so_far
        return max_distance
    so_far_set = set(so_far)
    for next_step in stars:
        if next_step not in so_far_set:
            max_distance = get_longest_route(so_far + [next_step], max_distance)
    return max_distance

print get_shortest_route()
print get_longest_route()
