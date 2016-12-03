import math
import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def is_prime(value):
    for d in xrange(2, value):
        if value % d == 0:
            return False
    return True


PRIMES = []
for p in xrange(2, 10001):
    if is_prime(p):
        PRIMES.append(p)


def get_prime_factors(value):
    exponents = []
    for p in PRIMES:
        exponents.append(0)
        while True:
            if value % p == 0:
                exponents[-1] += 1
                value /= p
            else:
                break
        if value == 1:
            break
    return exponents


def prod(value_list):
    p = 1
    for value in value_list:
        p *= value
    return p


def get_divisors(value):
    max_exponents = get_prime_factors(value)
    exponents = [0] * len(max_exponents)
    divisors = []
    while True:
        divisors.append(prod([p**e for p, e in zip(PRIMES, exponents)]))
        overflow = True
        for idx in xrange(1, len(exponents) + 1):
            if overflow:
                exponents[-idx] += 1
            if exponents[-idx] > max_exponents[-idx]:
                exponents[-idx] = 0
                overflow = True
            else:
                overflow = False
        if overflow:
            break
    return divisors


def number_of_presents(house_number):
    presents = 0
    first_elf = int(math.ceil(house_number / 50.0))
    for divisor in get_divisors(house_number):
        if divisor >= first_elf:
            presents += divisor * 11
    return presents


with open(input_filename, 'r') as f:
    min_present_count = int(f.read())

# n = 1000000
# n = 900000
n = 800000
# House 831600 got 35780206 presents.
n = 700000
# -

# 100k = cca 3min
# 800k -> 24min

while True:
    n += 1
    presents = number_of_presents(n)
    # presents = number_of_presents_silly(n)
    if presents >= min_present_count:
        break
    if n % 1000 == 0:
        print 'House %d got %d presents.' % (n, presents)

print 'House %d got %d presents.' % (n, number_of_presents(n))
