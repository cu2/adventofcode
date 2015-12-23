import copy
import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


SPELLS = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']


def cast_spell(spell, player, boss):
    if spell == 'Magic Missile':
        mana_cost = 53
        if mana_cost > player['mana']:
            return False
        boss['hp'] -= 4
    elif spell == 'Drain':
        mana_cost = 73
        if mana_cost > player['mana']:
            return False
        boss['hp'] -= 2
        player['hp'] += 2
    elif spell == 'Shield':
        mana_cost = 113
        if mana_cost > player['mana'] or player['shield_timer'] > 0:
            return False
        player['shield_timer'] = 6
    elif spell == 'Poison':
        mana_cost = 173
        if mana_cost > player['mana'] or player['poison_timer'] > 0:
            return False
        player['poison_timer'] = 6
    elif spell == 'Recharge':
        mana_cost = 229
        if mana_cost > player['mana'] or player['recharge_timer'] > 0:
            return False
        player['recharge_timer'] = 5
    else:
        raise Exception('Unknown spell')
    player['mana'] -= mana_cost
    player['mana_spent'] += mana_cost
    player['spell_history'].append(spell)
    return True


with open(input_filename, 'r') as f:
    raw_boss_stats = f.read()
raw_boss_hp, raw_boss_dmg = raw_boss_stats.split('\n')
boss = {
    'hp': int(raw_boss_hp.split(':')[1]),
    'dmg': int(raw_boss_dmg.split(':')[1]),
}
player = {
    'hp': 50,
    'mana': 500,
    'mana_spent': 0,
    'spell_history': [],
    'shield_timer': 0,
    'poison_timer': 0,
    'recharge_timer': 0,
}


difficulty = 'easy'
difficulty = 'hard'
# strategy = 'Poison, Magic Missile, Recharge, Poison, Magic Missile, Magic Missile, Magic Missile'.split(', ')
worlds = [(player, boss)]
min_mana_cost = None
turn = 0
while len(worlds):
    turn += 1
    new_worlds = []
    for player, boss in worlds:
        # your turn
        if difficulty == 'hard':
            player['hp'] -= 1
            if player['hp'] <= 0:
                # print 'L[%d] %s M%d HP%d:%d MM%d' % (turn, spell, new_player['mana'], new_player['hp'], new_boss['hp'], new_player['mana_spent'])
                continue
        if player['poison_timer'] > 0:
            boss['hp'] -= 3
            player['poison_timer'] -= 1
        if player['recharge_timer'] > 0:
            player['mana'] += 101
            player['recharge_timer'] -= 1
        if player['shield_timer'] > 0:
            player['shield_timer'] -= 1
        if boss['hp'] <= 0:
            if min_mana_cost is None or player['mana_spent'] < min_mana_cost:
                min_mana_cost = player['mana_spent']
            print 'W[%d] M%d HP%d:%d MM%d(%s)' % (turn, player['mana'], player['hp'], boss['hp'], player['mana_spent'], ', '.join(player['spell_history']))
            continue
        for spell in SPELLS:
            new_player = copy.deepcopy(player)
            new_boss = copy.deepcopy(boss)
            if cast_spell(spell, new_player, new_boss):
                # boss' turn
                if new_player['poison_timer'] > 0:
                    new_boss['hp'] -= 3
                    new_player['poison_timer'] -= 1
                if new_boss['hp'] <= 0:
                    if min_mana_cost is None or new_player['mana_spent'] < min_mana_cost:
                        min_mana_cost = new_player['mana_spent']
                    print 'W[%d] %s M%d HP%d:%d MM%d(%s)' % (turn, spell, new_player['mana'], new_player['hp'], new_boss['hp'], new_player['mana_spent'], ', '.join(new_player['spell_history']))
                    continue
                if new_player['recharge_timer'] > 0:
                    new_player['mana'] += 101
                    new_player['recharge_timer'] -= 1
                if new_player['shield_timer'] > 0:
                    new_player['hp'] -= new_boss['dmg'] - 7
                    new_player['shield_timer'] -= 1
                else:
                    new_player['hp'] -= new_boss['dmg']
                if new_player['hp'] <= 0:
                    # print 'L[%d] %s M%d HP%d:%d MM%d' % (turn, spell, new_player['mana'], new_player['hp'], new_boss['hp'], new_player['mana_spent'])
                    continue
                new_worlds.append((new_player, new_boss))
                # print '[%d] %s M%d HP%d:%d' % (turn, spell, new_player['mana'], new_player['hp'], new_boss['hp'])
    worlds = new_worlds
    if turn >= 10:
        break

print min_mana_cost
