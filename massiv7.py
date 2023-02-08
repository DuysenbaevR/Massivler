#7) Введите с клавиатуры в массив пять целочисленных значений.
# Выведите их в одну строку через запятую. Получите для массива среднее арифметическое.

n = int(input('Massiv uzinligin kiritin: '))
a = []
s = ''
sum = 0
for i in range(n):
    a.append(int(input('Manis kiritin:  ')))
    sum += a[i]
for k in range(n):
    print(a[k], end=", ")
print(f"Orta arifmetigi: {sum/n}")