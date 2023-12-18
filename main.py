def add_peoples():
    flag = True
    while flag:
        n = input('Какого сотрудника хотите добавить? Доступны варианты: Важный - либо 1; Рядовой - либо 2; Новый - либо 3: ').lower()
        if n == 'важный' or '1':
            n1 = input('Введите ФИО сотрудника, дату рождения и его телефон, а также его индекс в компании: ')
            top.append(n1)
        elif n == 'рядовой' or '2':
            n1 = input('Введите ФИО сотрудника, дату рождения и его телефон, а также его индекс в компании: ')
            off.append(n1)
        elif n == 'новый' or '3':
            n1 = input('Введите ФИО сотрудника, дату рождения и его телефон, а также его индекс в компании: ')
            new.append(n1)
        print('Сотрудник добавлен.')
        prodolzhenie = input('Хотите еще добавить сотрудника? ').lower()
        if prodolzhenie == 'да':
            continue
        else:
            flag = False


def clear_peoples():
    flag = True
    while flag:
        index = input('Введите индекс сотрудника которого хотите убрать из базы данных: ')
        for i in range(len(top)):
            if index in top[i]:
                del top[i]

        for i in range(len(off)):
            if index in off[i]:
                del off[i]

        for i in range(len(new)):
            if index in new[i]:
                del new[i]
        esli_hochet_eshe_ydalit = input('Хотите еще удалить сотрудника? ').lower()
        if esli_hochet_eshe_ydalit == 'да':
            continue
        elif esli_hochet_eshe_ydalit == 'нет':
            flag = False


print('привтствую! Меня зовут Константин и я создал эту программу.')
print('В ней вы можете добавлять ваших сотрудников в определенные списки, такие как: 1. Важные сотрудники; 2. Рядовые '
      'сотрудники; 3. Новые сотрудники. Таже сотрудников можно удалять из списка, если они были уволены.'
      'Также вы можете посмотреть списки ваших сотрудников аналогично добавлению.')
top = []
off = []
new = []

flag1 = True
while flag1:
    add = input('Что вы хотите сделать? Добавить или удалить? Или посмотреть все списки?').lower()
    if add == 'добавить':
        add_peoples()
    elif add == 'удалить':
        clear_peoples()
    elif add == 'посмотреть все списки':
        print(*top, sep='\n')
        print(*off, sep='\n')
        print(*new, sep='\n')
    vopros = input('Хотите продолжить?').lower()
    if vopros == 'да':
        continue
    elif vopros == 'нет':
        flag1 = False

print('Программа завершена, всего доброго!')
