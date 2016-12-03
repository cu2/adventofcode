import os
import re
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


deers = []
r = re.compile('([a-zA-Z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
with open(input_filename, 'r') as f:
    for line in f:
        name, speed, endurance, rest = r.match(line.strip()).groups()
        deers.append({
            'name': name,
            'pos': 0,
            'time_in_cycle': 0,
            'point': 0,
            'speed': int(speed),
            'endurance': int(endurance),
            'rest': int(rest),
            'avg_speed': 1.0 * int(speed) * int(endurance) / (int(endurance) + int(rest)),
        })

deers.sort(key=lambda deer: deer['avg_speed'], reverse=True)
fastest_deer = deers[0]

total_seconds = 2503

full_cycle_count = total_seconds / (fastest_deer['endurance'] + fastest_deer['rest'])
full_cycle_km = full_cycle_count * fastest_deer['endurance'] * fastest_deer['speed']

remainder_seconds = total_seconds - full_cycle_count * (fastest_deer['endurance'] + fastest_deer['rest'])
if remainder_seconds > fastest_deer['endurance']:
    remainder_seconds = fastest_deer['endurance']
remainder_km = remainder_seconds * fastest_deer['speed']

print full_cycle_km + remainder_km


for sec in xrange(total_seconds):
    max_pos = 0
    for deer in deers:
        if deer['time_in_cycle'] < deer['endurance']:
            deer['pos'] += deer['speed']
        if deer['time_in_cycle'] < deer['endurance'] + deer['rest'] - 1:
            deer['time_in_cycle'] += 1
        else:
            deer['time_in_cycle'] = 0
        if deer['pos'] > max_pos:
            max_pos = deer['pos']
    for deer in deers:
        if deer['pos'] == max_pos:
            deer['point'] += 1

deers.sort(key=lambda deer: deer['point'], reverse=True)
print deers[0]['point']
