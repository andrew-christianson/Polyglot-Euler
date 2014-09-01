
class memoize(object):

    def __init__(self, func):
        self.func = func
        self.mdict = {}

    def __call__(self, arg):
        try:
            return self.mdict[arg]
        except KeyError:
            self.mdict[arg] = self.func(arg)
            return self.mdict[arg]

@memoize
def isprime(num):
    if num == 2:
        return True
    bound = math.sqrt(num)
    if num & 1 == 0:
        return False
    for cfactor in xrange(3, int(bound + 1)):
        if num % cfactor == 0:
            return False
    return True

def cfactor(num):
    inum = num
    factors = set()
    while True:
        for fac in xrange(2, int(math.sqrt(num)) + 1):
            if num % fac == 0:
                factors.add(fac)
                factors.add(num)
                continue
        break
    print(sorted(list(factors)))
    return factors