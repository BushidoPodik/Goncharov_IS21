import random
N = random.randrange(2, 21)
K = random.randrange(1, N)
print('N = ', N)
print('K = ', K)
a = [i+1 for i in range(N)]
print('список:\n', a)
for i in range(N-1, K-1, -1):
    a[i] = a[i-K]
for i in range(0, K):
    a[i] = 0
print('измененный список 2:\n', a)
