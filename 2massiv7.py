#11) Дан массив из N элементов в диапазоне [100;300].
# Сжать массив, оставив в нем только те элементы, сумма цифр которых четная.
import random

a = []
count = 0
n = int(input('Massv olshemin kiritin: '))
for i in range(n):
    a.append(random.randrange(100, 300))
    if a[i] % 2 == 1:
        count += 1
print(a)
for k in range(count):
    index = 0
    for j in range(n):
        if a[j] % 2 == 1:
            index = j
    a.remove(a[index])
print(a)