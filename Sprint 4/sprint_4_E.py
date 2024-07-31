# line1 = 'ezhgeljkablzwnvuwqvp'
# line2 = 'gbpdcvkumyfxillgnqrv'


hashes = {}

from random import randint
def generater_string():
    temp = ''
    len_string = randint(10, 100)
    for i in range(1, len_string):
        temp += chr(randint(97, 122))
    return temp


def get_polynomial_hash(line, q, m):
    n = len(line)
    q_power = 1
    hash_value = 0
    for i in range(n):
        num_char = ord(line[n - 1 - i]) % m
        hash_value = (hash_value + num_char * q_power) % m
        q_power = (q_power * q) % m
    return(hash_value)

q = 1000
m = 123987123
# get_polynomial_hash(line2, q, m)

flag = True
n = 2000
while flag == True or n > 0:
    n -= 1
    line = generater_string()
    hash_value = get_polynomial_hash(line, q, m)

    if hash_value not in hashes:
        hashes[hash_value] = line
    elif hash_value in hashes:
        print(line)
        print(hash_value)
        print('='*200)
        print(line)
        print(hashes[hash_value])
        print('='*200)
        print('\n')
        flag = False

