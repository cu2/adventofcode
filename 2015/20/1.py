import math
import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def get_sum_divisors(exponents):
    num, sum_divisors = 1, 1
    for prime, exponent in zip(PRIMES, exponents):
        num *= prime**exponent
        sum_divisors *= (prime**(exponent+1) - 1) / (prime - 1)
    return num, sum_divisors


def max_exponent(prime, min_sum_divisors):
    return int(math.ceil(math.log(1 + min_sum_divisors * (prime-1), prime) - 1))


with open(input_filename, 'r') as f:
    min_present_count = int(f.read())
min_sum_divisors = min_present_count / 10

max_exponents = [max_exponent(prime, min_sum_divisors) for prime in PRIMES]

lowest_house_number = None
exponents = [0] * len(max_exponents)
while True:
    exponents[0] = 0
    num, sum_divisors = get_sum_divisors(exponents)
    exponents[0] = int(math.ceil(math.log(1.0 * min_sum_divisors / sum_divisors + 1, 2) - 1))
    if exponents[0] >= 0:
        num, sum_divisors = get_sum_divisors(exponents)
        if lowest_house_number is None or num < lowest_house_number:
            lowest_house_number = num
            # print num, exponents
    overflow = False
    exponents[-1] += 1
    for idx in xrange(1, len(exponents)):
        if overflow:
            exponents[-idx] += 1
        if exponents[-idx] > max_exponents[-idx]:
            exponents[-idx] = 0
            overflow = True
        else:
            overflow = False
    if overflow:
        break

print lowest_house_number
