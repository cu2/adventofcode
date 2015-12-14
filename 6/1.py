class Grid(object):
    lights = {}
    on_count = 0

    def __init__(self, width, height):
        for x in xrange(width):
            for y in xrange(height):
                self.lights[(x, y)] = 0

    def operate(self, from_coord, until_coord, cmd):
        x1, y1 = from_coord
        x2, y2 = until_coord
        for x in xrange(min(x1, x2), max(x1, x2) + 1):
            for y in xrange(min(y1, y2), max(y1, y2) + 1):
                before_state = self.lights[(x, y)]
                if cmd == 'on':
                    self.lights[(x, y)] = 1
                elif cmd == 'off':
                    self.lights[(x, y)] = 0
                else:
                    self.lights[(x, y)] = 1 - self.lights[(x, y)]
                self.on_count += self.lights[(x, y)] - before_state


def split_coord(str_coord):
    x, y = str_coord.split(',')
    return int(x), int(y)


grid = Grid(1000, 1000)

with open('input', 'r') as f:
    for line in f:
        tokens = line.rstrip('\n').split(' ')
        if tokens[0] == 'turn':
            _, cmd, from_coord, _, until_coord = tokens
        else:
            cmd, from_coord, _, until_coord = tokens
        grid.operate(
            split_coord(from_coord),
            split_coord(until_coord),
            cmd
        )

print grid.on_count
