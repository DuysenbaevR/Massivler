#3) Найти наименьший элемент одномерного массива, состоящего из n элементов. Элементы вводятся с клавиатуры.

n  = int(input('Massiv uzinligin kiritin: '))
a = []
for i in range(n):
    a.append(int(input('Manis kiritin: ')))
print(min(a))