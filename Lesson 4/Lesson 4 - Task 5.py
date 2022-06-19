from functools import reduce
from operator import mul

print(reduce(mul, [x for x in range(100, 1001, 2)]))
