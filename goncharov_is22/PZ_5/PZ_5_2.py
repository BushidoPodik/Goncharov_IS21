import random


def invertdigits(k):
    s = str(k['K'])
    s_new = s[::-1]
    k['K'] = int(s_new)


R = {'K': None}
for i in range(5):
    R['K'] = random.randrange(1, 10000)
    print("Число ", i + 1, ": ", R['K'])
    invertdigits(R)
    print('Измененное = ', R['K'])
