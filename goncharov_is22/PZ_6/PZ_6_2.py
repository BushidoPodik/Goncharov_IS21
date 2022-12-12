import random
N = random.randrange(2, 24)
print("N = ", N)
a = [random.randrange(1, 24) for i in range(N)]
print("Array:")
print(a)
L_Min = []
for i in range(1, N-1):
    if a[i-1] > a[i] and a[i] < a[i+1]:
        L_Min.append(a[i])
print("локальные минимумы:")
print(L_Min)
if L_Min:
    print(max(L_Min))
