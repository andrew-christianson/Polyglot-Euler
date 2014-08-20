from __future__ import print_function


def gen_fib(max_val):
    l1, l2 = 1,1
    nval = 0
    while nval < max_val:
        nval = sum([l1,l2])
        l1, l2 = l2, nval
        yield nval

if __name__ == "__main__":
    res = sum(i for i in gen_fib(4000000)
              if i & 1 == 0)
    print("The answer to Euler Problem 2 is {}".format(res))