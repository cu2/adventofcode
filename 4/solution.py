import hashlib

secret_key = 'iwrupvqb'

answer = 1
while hashlib.md5(secret_key + str(answer)).hexdigest()[:5] != '00000':
    answer += 1
print answer

answer = 1
while hashlib.md5(secret_key + str(answer)).hexdigest()[:6] != '000000':
    answer += 1
print answer
