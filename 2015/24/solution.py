import itertools


def load_input():
    import os
    input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')
    packages = []
    with open(input_filename, 'r') as f:
        for line in f:
            packages.append(int(line))
    return sorted(packages)


def get_qe(packages):
    qe = 1
    for p in packages:
        qe *= p
    return qe


def find_optimal_first_group(packages, weight_per_group):
    number_of_packages = len(packages)
    for number_of_packages_in_first_group in xrange(1, number_of_packages + 1):
        min_qe = None
        for packages_in_first_group in itertools.combinations(packages, number_of_packages_in_first_group):
            if sum(packages_in_first_group) == weight_per_group:
                qe = get_qe(packages_in_first_group)
                if min_qe is None or qe < min_qe:
                    min_qe = qe
        if min_qe is not None:
            return min_qe


packages = load_input()
total_weight = sum(packages)
print find_optimal_first_group(packages, total_weight / 3)
print find_optimal_first_group(packages, total_weight / 4)
