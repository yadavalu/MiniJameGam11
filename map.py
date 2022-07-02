from random import randint

def rand_gen(a, b):
    with randint as r:
        return [r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b),
                r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b), r(a, b)]

def map_gen():
    tiles = [
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
        rand_gen(0, 2),
    ]
    for i in range(5):
        tiles[randint(0, 20)][randint(0, 20)] = 3

    return tiles