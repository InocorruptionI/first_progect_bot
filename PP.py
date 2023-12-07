month = [31, 28, 30, 31, 31, 30, 30, 31]
n = int(input('Введи число месяца:'))
s = int(input('Введи введи число последнего твоего выхода во вторую смену:'))
while month[n - 1] > s:
    holiday_1 = 0
    holiday_2 = 0
    if holiday_1 <= month[n - 1] or holiday_2 <= month[n - 1]:
        holiday_1 = s + 1
        holiday_2 = s + 2
    else:
        break
    s += 4
    print('Первый выхдной:', holiday_1, 'Второй выходной:', holiday_2)

