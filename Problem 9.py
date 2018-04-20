def is_triple(a,b,c):
    return a ** 2 + b ** 2 == c ** 2


def triple():
    for a in range(1,1000):
        for b in range(1,1000):
            c = 1000 - a - b
            if c < 0:
                continue
            if is_triple(a,b,c):
                return a,b,c

def main():
    a,b,c = triple()
    print((a,b,c))
    print("The answer to Euler Problem 9 is", a*b*c)

main()
