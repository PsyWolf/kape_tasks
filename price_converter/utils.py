import math

# rounding up numbers by decimal places
# i.e. decimals=1 will round up to nearest 0.1 place
# decimals=-1 will round up to nearest 10 place
def round_up(num, decimals=0):
    multi = 10 ** decimals
    return math.ceil(num * multi) / multi
