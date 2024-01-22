n = int(input())
list1 = []
for i in range(n):
    s = input()
    list1.append(s)
    print(list1[i])

while n > 0:
    print(list1[n - 1])
    n -= 1

c = int(input('введите число: '))
m = int(input('введите число: '))


def test(m, c):
    res = m + c
    return res


b = test(n, c)
print(b)

