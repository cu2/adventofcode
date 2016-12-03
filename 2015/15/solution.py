import os
import re
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def evaluate_cookie(ingredients, amounts):
    scores = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0,
    }
    for name, amount in amounts.iteritems():
        for factor in scores:
            scores[factor] += amount * ingredients[name][factor]
    total_score = 1
    for factor in scores:
        if scores[factor] < 0:
            scores[factor] = 0
        total_score *= scores[factor]
    return total_score


def get_cookie_calories(ingredients, amounts):
    return sum([amount * ingredients[name]['calories'] for name, amount in amounts.iteritems()])


ingredients = {}
r = re.compile('([a-zA-Z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
with open(input_filename, 'r') as f:
    for line in f:
        name, capacity, durability, flavor, texture, calories = r.match(line.strip()).groups()
        ingredients[name] = {
            'capacity': int(capacity),
            'durability': int(durability),
            'flavor': int(flavor),
            'texture': int(texture),
            'calories': int(calories),
        }

ingredient_list = sorted(ingredients.keys())

def get_best_combo(so_far, max_score=0, calories_required=None):
    if len(so_far) == len(ingredient_list):
        amounts = dict([(key, value) for key, value in zip(ingredient_list, so_far)])
        if calories_required is not None:
            if get_cookie_calories(ingredients, amounts) != calories_required:
                return max_score
        score = evaluate_cookie(ingredients, amounts)
        if score > max_score:
            max_score = score
        return max_score
    so_far_amount = sum(so_far)
    if len(so_far) == len(ingredient_list) - 1:
        amount = 100 - so_far_amount
        max_score = get_best_combo(so_far + [amount], max_score, calories_required)
    else:
        for amount in xrange(101):
            if so_far_amount + amount > 100:
                continue
            max_score = get_best_combo(so_far + [amount], max_score, calories_required)
    return max_score

print get_best_combo([], 0)

print get_best_combo([], 0, calories_required=500)
