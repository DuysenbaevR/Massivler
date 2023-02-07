#1) Найти сумму элементов одномерного массива. Размер произвольный. Элементы вводятся с клавиатуры.

n = int(input('Masssiv uzinligin kiritin: '))
a = []
sum = 0
for i in range(n):
  a.append(int(input('Manis kiritin: ')))
  sum += a[i]
print(f"Elementler qosindisi: {sum}")