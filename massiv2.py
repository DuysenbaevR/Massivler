#2)  Найти сумму элементов массива с четными номерами, содержащего N элементов. Элементы вводятся с клавиатуры.

n = int(input('Massiv uzinlgin kiritin: '))
sum = 0
a = []
for i in range(n):
    a.append(int(input('Manis kiritin: ')))
    if a[i] % 2 == 0:
        sum += a[i]
print(f"Jup elementler qosindisi: {sum}")