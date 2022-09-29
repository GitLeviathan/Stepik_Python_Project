import random


def number_guessing():
    print('Добро пожаловать в числовую угадайку. В каком промежутке мне загадать число? Напиши два числа.')
    guessing_gap = []
    while len(guessing_gap) < 2:
        temp = input()
        if temp.isdigit() == True:
            guessing_gap.append(int(temp))
        else:
            print('Напиши пожалуйста число')
    guessing_gap.sort()
    hidden_number = random.randrange(guessing_gap[0], guessing_gap[1])
    your_number = 0
    attempts = 0
    print('Добро пожаловать в числовую угадайку. Как думаешь, какое число от', guessing_gap[0], 'до', guessing_gap[1], 'я загадал?')
    while hidden_number != your_number:
        your_number = input()
        if your_number == '':
            print('А может быть все-таки введем целое число от ', guessing_gap[0], ' до ', guessing_gap[0], '?', sep = '')
        elif int(your_number) in range(1, 100):
            if int(your_number) > hidden_number:
                print('Слишком много, попробуйте еще раз')
            elif int(your_number) < hidden_number:
                print('Слишком мало, попробуйте еще раз')
            else:
                break
        else:
            print('А может быть все-таки введем целое число от ', guessing_gap[0], ' до ', guessing_gap[0], '?', sep = '')
        attempts += 1
    print('Вы угадали, поздравляем! Вы угадали с', attempts, 'попытки')
    print('Хотетие сыграть ещё? Да или Нет?')
    if input() == "да":
        number_guessing()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

def secure_password_generator():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    exceptions = 'il1Lo0O'
    charm = ''
    print('Значит тебе нужен безопасный уникальный пароль? Тогда ты обратился по адрес! Какие условия для пороля?')
    print('Сколько нужно паролей?')
    count = int(input())
    print('Из сколько символов должны состоять пароли?')
    password_len = (int(input()))
    print('Включаем цифры в пароли? Да/Нет')
    if input().lower() == 'да':
        charm += digits
    print('Включаем строчные буквы в пароли? Да/Нет')
    if input().lower() == 'да':
        charm += lowercase_letters
    print('Включаем заглавные буквы в пароли? Да/Нет')
    if input().lower() == 'да':
        charm += uppercase_letters
    print('Включаем символы в пароли? Да/Нет')
    if input().lower() == 'да':
        charm += punctuation
    print('Будем исключать неоднозначные символы (il1Lo0O)? Да/Нет')
    if input().lower() == 'да':
        for i in range(len(exceptions)):
            charm.replace(exceptions[i], '')
    for _ in range(count):
        print(''.join(random.sample(charm, password_len)))

def caesar_cipher():
    en = 'abcdefghijklmnopqrstuvwxyz'
    ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    print('Что ты хочешь сделать?', '1) Зашифровать текст', '2) Расшифровать текст', sep='\n')
    cipher = ''
    while cipher == '':
        cipher = input()
        if cipher not in ['1', '2']:
            print('Так мы шифруем или расшифровываем?', '1) Зашифровать текст', '2) Расшифровать текст', sep='\n')
            teamp = ''
    print('С каким языком будем работать? en/ru')
    language = ''
    while language == '':
        language = input()
        if language not in ['en', 'ru']:
            print('Так какой язык? en/ru')
            language = ''
    print('На соклько букв будем сдвигать?')
    count = input()
    if count.isdigit() != True:
        print('Введите только число, на соклько букв будем сдвигать')
    else:
        count = int(count)
    if cipher == '1':
        new_en = en[count:] + en[:count]
        new_ru = ru[count:] + ru[:count]
    elif cipher == '2':
        count = -count
        new_en = en[count:] + en[:count]
        new_ru = ru[count:] + ru[:count]
    print('Введите текст, который нужно преобразовать')
    text = input().lower()
    new_text = ''
    if language == 'en':
        for i in range(len(text)):
            ind = en.index(text[i])
            new_text += new_en[ind]
    if language == 'ru':
        for i in range(len(text)):
            if 'ё' in text:
                while 'ё' in text:
                    text = text.replace('ё', 'е')
            new_text += new_ru[ru.index(text[i])]
    print(new_text.capitalize())


print('Приветствую! Напиши номер программы, которую зочешь запустить', '1) Угадайка чисел', '2) Генератор безопасных паролей', '3) Шифр Цезаря', sep = '\n')
number = input()
if number == '1':
    number_guessing()
elif number == '2':
    secure_password_generator()
elif number == '3':
    caesar_cipher()