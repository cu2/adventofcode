import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')


def inc_char(char):
    if char == 'z':
        return 1, 'a'
    return 0, chr(ord(char) + 1)


def inc_pw(pw):
    pw_seq = [ch for ch in pw]
    overflow, pw_seq[-1] = inc_char(pw_seq[-1])
    if overflow:
        for rpos in xrange(2, len(pw_seq) + 1):
            overflow, pw_seq[-rpos] = inc_char(pw_seq[-rpos])
            if overflow == 0:
                break
    return ''.join(pw_seq)


def is_valid(pw):
    seq_len = 1
    seq_start = 0
    has_seq_3 = False
    last_double_pos = -2
    double_count = 0
    for pos, ch in enumerate(pw):
        if ch in {'i', 'o', 'l'}:
            return False
        if pos:
            if ord(ch) == ord(pw[pos - 1]) + 1:
                seq_len += 1
                if seq_len >= 3:
                    has_seq_3 = True
            else:
                seq_len = 1
                seq_start = pos
            if ch == pw[pos - 1]:
                if pos - 1 > last_double_pos + 1:
                    double_count += 1
                    last_double_pos = pos - 1
    return has_seq_3 and double_count >= 2


def next_pw(pw, verbose=False):
    cnt = 0
    while True:
        cnt += 1
        if cnt % 100000 == 0:
            if verbose:
                print pw, cnt
        pw = inc_pw(pw)
        if is_valid(pw):
            return pw


with open(input_filename, 'r') as f:
    current_password = f.read()

pw = next_pw(current_password, verbose=True)
print pw

pw = next_pw(pw, verbose=True)
print pw
