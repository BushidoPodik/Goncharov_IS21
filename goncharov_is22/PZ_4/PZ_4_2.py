import random
N = random.randrange(1, 10000000)
print("N = ", N)
q = N
while q >= 1:
    r = q % 10
    print(r, end="; ")
    q = int(q/10)
