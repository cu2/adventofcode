import os
import re
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
tickertape_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tickertape')

aunts = []
r = re.compile('Sue (\d+): (.+)')
with open(input_filename, 'r') as f:
    for line in f:
        aunt_no, raw_items = r.match(line.strip()).groups()
        items = {}
        for raw_item in raw_items.split(','):
            key, value = raw_item.strip().split(':')
            items[key.strip()] = int(value.strip())
        aunts.append(items)

tickertape = {}
with open(tickertape_filename, 'r') as f:
    for line in f:
        key, value = line.strip().split(':')
        tickertape[key.strip()] = int(value.strip())


def suspect(aunt, tickertape):
    for key, value in tickertape.iteritems():
        if key not in aunt:
            continue
        if aunt[key] != value:
            return False
    return True


def fixed_suspect(aunt, tickertape):
    for key, value in tickertape.iteritems():
        if key not in aunt:
            continue
        if key in {'cats', 'trees'}:
            if aunt[key] <= value:
                return False
        elif key in {'pomeranians', 'goldfish'}:
            if aunt[key] >= value:
                return False
        else:
            if aunt[key] != value:
                return False
    return True


for idx, aunt in enumerate(aunts):
    if suspect(aunt, tickertape):
        print idx + 1

for idx, aunt in enumerate(aunts):
    if fixed_suspect(aunt, tickertape):
        print idx + 1
