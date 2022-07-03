from itertools import count

for i in count(n := int(input())):
    print(i)
    if i > n + 10:
        break

from itertools import cycle

j = 1
for i in cycle(input()):
    print(i)
    j += 1
    if j > 10:
        break
