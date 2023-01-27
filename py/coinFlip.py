# written to test break points

import random

heads = 0
tails = 0

for i in range(1, 1001):
    toss = random.randint(0,1)
    if toss == 1:
        heads = heads + 1
    elif toss == 0:
        tails = tails + 1
    if i == 500:
        print('Halfway done!')

print('Heads came up ' + str(heads) + ' times.')
print('Tails came up ' + str(tails) + ' times.')
