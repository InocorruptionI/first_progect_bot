import itertools
num = int(input('Введите число: '))

list = []

while num > 0:
    word = set(input())
    list.append(word)
    num -= 1

print(list)
