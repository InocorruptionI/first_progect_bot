ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punktuation = '!#$%&*+-=?@^_ ,.'

txt = input('Введите текст')
choice = input('Если хотите защифровать текст - напишите: 1; Если хотите дешифровать текст - напишите: 2: ')
n = int(input('Введите ключ: '))
desh_txt = ''
if choice == '1':
    for i in txt:
        if i in ru_lower:
            b = (ru_lower.index(i) + n) % 32
            i = ru_lower[b]
            desh_txt += i
        elif i in ru_upper:
            b = (ru_upper.index(i) + n) % 32
            i = ru_upper[b]
            desh_txt += i
        if i in en_upper:
            b = (en_upper.index(i) + n) % 26
            i = en_upper[b]
            desh_txt += i
        if i in en_lower:
            b = (en_lower.index(i) + n) % 26
            i = en_lower[b]
            desh_txt += i
        if i in punktuation:
            desh_txt += i
elif choice == '2':
    for i in txt:
        if i in ru_lower:
            b = (ru_lower.index(i) - n) % 32
            i = ru_lower[b]
            desh_txt += i
        elif i in ru_upper:
            b = (ru_upper.index(i) - n) % 32
            i = ru_upper[b]
            desh_txt += i
        if i in en_upper:
            b = (en_upper.index(i) - n) % 26
            i = en_upper[b]
            desh_txt += i
        if i in en_lower:
            b = (en_lower.index(i) - n) % 26
            i = en_lower[b]
            desh_txt += i
        if i in punktuation:
            desh_txt += i
print(desh_txt)
