from random import randint

n = int(input("Введите размер списка: "))
lst = [randint(1,50) for i in range(n)]
print(lst)

min = int(input("Введите нижнюю границу диапазона: "))
max = int(input("Введите верхнюю границу диапазона: "))

lstIndex = list()

for i in range(n):
    if min<=lst[i]<=max:
        lstIndex.append(i)

print(lstIndex)