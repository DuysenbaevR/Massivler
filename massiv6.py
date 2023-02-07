#6) Массив А вводится с клавиатуры. Сформировать новый массив В,
# состоящий из четных элементов массива А. Элементы вводятся с клавиатуры. Размер n.

n = int(input('Massiv uzinligin kirtin: '))
a = []
b = []
for i in range(n):
    a.append(int(input('Manis kirtin: ')))
    if a[i] % 2 == 0:
        b.append(a[i])
for i in b:
    print(i)