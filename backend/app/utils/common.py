import random


def gen_random_word(num):
    seed = "abcdefghijklmnopqrstuvwxyz"
    sa = []
    for i in range(num):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt
