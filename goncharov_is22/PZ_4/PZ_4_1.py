print("Введите наименьшее число диапазона")
a = int(input())
print('введите наибольшее число диапазона')
b = int(input())
sum_ = 0
for i in range(a, b):
    sum_ += i
print(sum_)
