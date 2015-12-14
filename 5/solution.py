def vowel_count(s):
    return sum([int(ch in {'a', 'e', 'i', 'o', 'u'}) for ch in s])
    # return sum([s.count(vowel) for vowel in 'aeiou'])

def has_double(s):
    for idx, ch in enumerate(s[:-1]):
        if ch == s[idx + 1]:
            return True
    return False

def is_nice(s):
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return False
    if vowel_count(s) < 3:
        return False
    return has_double(s)

def has_double_pair(s):
    for idx, ch in enumerate(s[:-1]):
        pair = ch + s[idx + 1]
        if pair in s[:idx] or pair in s[idx + 2:]:
            return True
    return False

def has_split_double(s):
    for idx, ch in enumerate(s[:-2]):
        if ch == s[idx + 2]:
            return True
    return False

def is_really_nice(s):
    return has_double_pair(s) and has_split_double(s)


nice_string_count = 0
really_nice_string_count = 0

with open('input', 'r') as f:
    for line in f:
        if is_nice(line.strip('\n')):
            nice_string_count += 1
        if is_really_nice(line.strip('\n')):
            really_nice_string_count += 1

print nice_string_count
print really_nice_string_count
