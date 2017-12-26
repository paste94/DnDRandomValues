import json
from random import randint

import Constants


def get_tuple(cr):
    return select_random_tuple(get_table(cr))


def get_table(cr):
    with open('./files/CR_' + cr + '.txt', 'r') as readfile:
        table = json.load(readfile)
        return table


def select_random_tuple(table):
    perc = randint(1, 100)
    i = 0
    print 'ccc' + str(perc) + str(table[i][Constants.MIN_PERC])
    while i < len(table):
        if table[i][Constants.MIN_PERC] <= perc <= table[i][Constants.MAX_PERC]:
            print table[i]
            return table[i]
        i += 1
