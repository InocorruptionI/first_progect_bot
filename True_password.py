from random import *

digits = '0123456789'
lowercase_latters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_latters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
neodn = 'il1Lo0O'

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'

kol_pass = int(input('Сколько паролей вы хотите получить? '))
len_pass = int(input('Сколько символов будет включать пароль? '))
vkl_digits = input('Будем включать в пароль цифры ? ')
vkl_lovercase = input('Будем включать в пароль цифры в нижнем регистре? ')
vkl_uppercase = input('Будем включать в пароль буквы в верхнем регистре? ')
vkl_punctuation = input('Будем включать в пароль символы пунктуации? ')
iskl_neodn = input('Исключать неоднозначные символы? ')


def chars_1(chars_11, digits_1, lowercase, upperase, punctuation_1, vkl_digit, vkl_lover, vkl_upper, vkl_punct, iskl):
    if vkl_digit == 'нет':
        chars_11 = str(chars_11.replace(str(digits_1, '')))
    if vkl_lover == 'нет':
        chars_11 = str(chars_11.replace(lowercase, ''))
    if vkl_upper == 'нет':
        chars_11 = str(chars_11.replace(upperase, ''))
    if vkl_punct == 'нет':
        chars_11 = str(chars_11.replace(punctuation_1, ''))
    if iskl == 'да':
        chars_11 = str(chars_11.replace(iskl, ''))
    return chars_11


def generate_password(chars_12, len_password):
    password_generate = ''
    for i in range(len_password):
        password_generate += choice(chars_12)
    return password_generate


chars_1(chars, digits, lowercase_latters, uppercase_latters, punctuation, vkl_digits, vkl_lovercase, vkl_uppercase,
        vkl_punctuation, neodn)

for i in range(kol_pass):
    print(generate_password(chars, len_pass))
print('ВАШИ ПАРОЛИ')
