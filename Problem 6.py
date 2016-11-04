# Constraied to one-liners for this one
from __future__ import print_function

# I'm relatively satisfied here.  All computation is one line, following pep8
s, r = sum, list(range(101)); a = s(r) ** 2 - s(i ** 2 for i in r)
print("The answer to Euler Probelm 6 is", a)

# A true one liner disregarding pep8 could be:
# print("The answer to Euler Problem 6 is", sum(range(101))**2-sum(i**2 for i in range(101)))
