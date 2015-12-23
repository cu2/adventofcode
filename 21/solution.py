import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def does_player_win(player, boss):
    boss_hp = boss['hp']
    player_hp = player['hp']
    while True:
        boss_hp -= max(1, player['dmg'] - boss['arm'])
        if boss_hp <= 0:
            return True
        player_hp -= max(1, boss['dmg'] - player['arm'])
        if player_hp <= 0:
            return False


def load_shop():
    def parse_item(line):
        name, cost, dmg, arm = line.strip().split()
        return (name, int(cost), int(dmg), int(arm))
    weapons, armors, rings = [], [], []
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'weapons'), 'r') as f:
        for line in f:
            weapons.append(parse_item(line))
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'armors'), 'r') as f:
        for line in f:
            armors.append(parse_item(line))
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'rings'), 'r') as f:
        for line in f:
            rings.append(parse_item(line))
    return (weapons, armors, rings)


with open(input_filename, 'r') as f:
    raw_boss_stats = f.read()
raw_boss_hp, raw_boss_dmg, raw_boss_arm = raw_boss_stats.split('\n')
boss = {
    'hp': int(raw_boss_hp.split(':')[1]),
    'dmg': int(raw_boss_dmg.split(':')[1]),
    'arm': int(raw_boss_arm.split(':')[1]),
}
player = {
    'hp': 100,
    'dmg': 0,
    'arm': 0,
}

weapons, armors, rings = load_shop()
armors = [['', 0, 0, 0]] + armors
rings = [['', 0, 0, 0]] + rings

min_cost = None
for weapon in weapons:
    for armor in armors:
        for idx1, ring1 in enumerate(rings):
            for idx2, ring2 in enumerate(rings):
                if idx1 > 0 and idx1 >= idx2:
                    continue
                player = {
                    'hp': 100,
                    'dmg': weapon[2] + armor[2] + ring1[2] + ring2[2],
                    'arm': weapon[3] + armor[3] + ring1[3] + ring2[3],
                }
                if does_player_win(player, boss):
                    cost = weapon[1] + armor[1] + ring1[1] + ring2[1]
                    if min_cost is None or cost < min_cost:
                        min_cost = cost
                        # print player, weapon[0], armor[0], ring1[0], ring2[0], cost
print min_cost

max_cost = None
for weapon in weapons:
    for armor in armors:
        for idx1, ring1 in enumerate(rings):
            for idx2, ring2 in enumerate(rings):
                if idx1 > 0 and idx1 >= idx2:
                    continue
                player = {
                    'hp': 100,
                    'dmg': weapon[2] + armor[2] + ring1[2] + ring2[2],
                    'arm': weapon[3] + armor[3] + ring1[3] + ring2[3],
                }
                if not does_player_win(player, boss):
                    cost = weapon[1] + armor[1] + ring1[1] + ring2[1]
                    if max_cost is None or cost > max_cost:
                        max_cost = cost
                        # print player, weapon[0], armor[0], ring1[0], ring2[0], cost
print max_cost
