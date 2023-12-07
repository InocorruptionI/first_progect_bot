from random import *

word_list = ['ОСЕЛ', 'КОТ', 'ШРЕК', 'ФИОНА', 'ПРЯНЯ', 'ЧАМИНГ', 'ФЕЯ']


def get_word():
    word = choice(word_list)
    return word


def print_word(word_, list_):
    for i in word_:
        if i in list_:
            print(i, end=' ')
        else:
            print('_', end=' ')
    print()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = []
    for i in range(len(word)):
        word_completion.append('_')  # Столько букв в слове
    flag = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(*word_completion)
    while True:
        word_input = input('Введи сразу слово или букву: ').upper()
        if len(word_input) == 1:
            if word_input not in guessed_letters:
                guessed_letters.append(word_input)
                if word_input in word:
                    for i in range(len(word)):
                        if word[i] == word_input:
                            word_completion[i] = word_input
                    print(*word_completion, 'Вы угадали букву!')
                    break
                else:
                    tries -= 1
                    if tries == 0:
                        print('Ты проиграл', display_hangman(tries))
                    else:
                        print(display_hangman(tries), f'У тебя осталось попыток {tries}')
        if '_' not in word_completion:
            print('Вы выиграли!', *word_completion)
            break
        elif len(word_input) == len(word):
            if word_input == word:
                for i in range(len(word)):
                    word_completion[i] = word_input[i]
                print(*word_completion, 'Вы выиграли!')
                break
            else:
                tries -= 1
                print('Слово неверное!')
                print(display_hangman(tries), f'У тебя осталось попыток {tries}')
        if 1 < len(word_input) < len(word):
            tries -= 1
            print(display_hangman(tries))
            print('Слово не подходит')
        if tries == 0:
            print('Игра окончена.')
            break


play(get_word())
