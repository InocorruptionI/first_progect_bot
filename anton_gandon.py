num_words = int(input())
list_words = []
ant = 'anton'
counter = ''

while num_words != 0:
    word = input()
    list_words.append(word)
    num_words -= 1

for i in list_words:
    counter += i[0]
    for j in range(1, len(i)):
        if str(j) in counter:
            continue
        else:
            counter += i[j]
    counter += ' '

print(counter)
