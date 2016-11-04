from __future__ import print_function, division
import sys
import string

if sys.version_info.major == 2:
    import __builtin__
    builtins = __builtin__
    xrange = __builtin__.xrange
else:
    import builtins
    xrange = builtins.range

ALPHA_INDEX = {letter: idx + 1 for idx, letter in enumerate(string.ascii_uppercase)}


def name_val(name):
    return sum([ALPHA_INDEX[l] for l in name])


if __name__ == '__main__':
    res = 0
    with open("Problem 22.txt", "r") as fnames:
        names = fnames.read().replace("\"", "").split(",")
        names.sort()

    for idx, name in enumerate(names):
        res += (idx+1) * name_val(name)

    print("The answer to Euler Problem 22 is", res)
