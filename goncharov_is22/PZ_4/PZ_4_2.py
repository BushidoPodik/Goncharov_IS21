n = int(input('ведите число:'))
c = 0
s = 0
while n > 0:
    c += 1
    s += n % 10
    n //= 10
print(c, s)
