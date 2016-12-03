import hashlib
import os
input_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'input')

with open(input_filename, 'r') as f:
    secret_key = f.read()

answer = 1
while hashlib.md5(secret_key + str(answer)).hexdigest()[:5] != '00000':
    answer += 1
print answer

answer = 1
while hashlib.md5(secret_key + str(answer)).hexdigest()[:6] != '000000':
    answer += 1
print answer
