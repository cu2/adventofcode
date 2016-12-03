import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


WIDTH = 100
HEIGHT = 100


def sim(grids, from_grid, to_grid, stuck_corner=False):
    brightness = 0
    for y in xrange(1, HEIGHT + 1):
        for x in xrange(1, WIDTH + 1):
            neighbor_count = sum([
                grids[from_grid][y-1][x-1],
                grids[from_grid][y-1][x  ],
                grids[from_grid][y-1][x+1],
                grids[from_grid][y  ][x-1],
                grids[from_grid][y  ][x+1],
                grids[from_grid][y+1][x-1],
                grids[from_grid][y+1][x  ],
                grids[from_grid][y+1][x+1],
            ])
            next_state = 0
            if grids[from_grid][y][x] == 1:
                if neighbor_count in {2, 3}:
                    next_state = 1
            else:
                if neighbor_count == 3:
                    next_state = 1
            if stuck_corner:
                if x in {1, WIDTH} and y in {1, HEIGHT}:
                    next_state = 1
            grids[to_grid][y][x] = next_state
            brightness += next_state
    return brightness


def load_grid():
    grids = [
        [],
        [],
    ]
    grids[0].append([0] * (WIDTH + 2))
    with open(input_filename, 'r') as f:
        for line in f:
            grids[0].append([0])
            for cell in line.strip():
                grids[0][-1].append(1 if cell == '#' else 0)
            grids[0][-1].append(0)
    grids[0].append([0] * (WIDTH + 2))
    for _ in xrange(HEIGHT + 2):
        grids[1].append([0] * (WIDTH + 2))
    return grids


grids = load_grid()
for step in xrange(100):
    brightness = sim(grids, step % 2, 1 - step % 2)
print brightness


grids = load_grid()
for step in xrange(100):
    brightness = sim(grids, step % 2, 1 - step % 2, stuck_corner=True)
print brightness
