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
            if text[i] in en:
                new_text += new_en[en.index(text[i])]
            else:
                new_text += text[i]
    if language == 'ru':
        for i in range(len(text)):
            if 'ё' in text:
                while 'ё' in text:
                    text = text.replace('ё', 'е')
            if text[i] in ru:
                new_text += new_ru[ru.index(text[i])]
            else:
                new_text += text[i]
    print(new_text.capitalize())

def hangman():
    word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода', 'отец', 'проблема', 'час', 'право', 'нога', 'решение', 'дверь', 'образ', 'история', 'власть', 'закон', 'война', 'бог', 'голос', 'тысяча', 'книга', 'возможность', 'результат', 'ночь', 'стол', 'имя', 'область', 'статья', 'число', 'компания', 'народ', 'жена', 'группа', 'развитие', 'процесс', 'суд', 'условие', 'средство', 'начало', 'свет', 'пора', 'путь', 'душа', 'уровень', 'форма', 'связь', 'минута', 'улица', 'вечер', 'качество', 'мысль', 'дорога', 'мать', 'действие', 'месяц', 'государство', 'язык', 'любовь', 'взгляд', 'мама', 'век', 'школа', 'цель', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент', 'театр', 'письмо', 'утро', 'помощь', 'ситуация', 'роль', 'рубль', 'смысл', 'состояние', 'квартира', 'орган', 'внимание', 'тело', 'труд', 'сын']
    def get_word():
        choice = random.choice(word_list).upper()
        return choice

    def display_hangman(mistakes):
        stages = [
            '''
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            ''',
            '''
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            ''',
            '''
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            ''']
        return stages[mistakes]

    next_game = '+'

    def play():
        word = get_word()
        l = len(word)
        mistakes = 0
        inputs = []

        answer = ['_' for _ in range(l)]
        print('Привет! Давай сыграем в виселицу! Я буду загадывать слова, а ты их угадывать. Я загадал, можешь начинать')

        while mistakes < 6:
            while '_' in answer:
                print('Напиши букву, которая по твоему может оказаться в загаданном слове')
                letter = input().upper()
                if letter in inputs:
                    print('Ты уже называл эту букву')
                    break
                if letter in word:
                    for i in range(l):
                        if word[i] == letter:
                            answer[i] = letter
                    print('Таак, одну букву ты угадал, давай дальше')
                else:
                    mistakes += 1
                    print('Ты не угадал, сделай ещё попытку')

                print(display_hangman(mistakes))
                inputs.append(letter)
                break
            else:
                print(
                    'Congratulations! You saved your ass this time - you guessed the word! Mr. Hangman will generously spare your life.')
                global next_game
                next_game = input('''Although, if you\'re still willing to press your luck and eventually die on the gallows, of course -
                you're welcome to start the Game once again. Just tap '+', little shit, let's see what you've got!
                Or press '-' and get out of here for good, man: ''')
                break

        else:
            print('У тебя закончились попытки, ты проиграл')
            print('Ты был близок, я загадал слово', word)
            next_game = input('Если хочешь сыграть ещё раз поставь "+"')

    while next_game == '+':
        play()
    else:
        print('Было приятно сыграть, пока!')

print('Приветствую! Напиши номер программы, которую зочешь запустить', '1) Угадайка чисел', '2) Генератор безопасных паролей', '3) Шифр Цезаря', '4) Виселица (пока только на русском)', sep = '\n')
number = input()
if number == '1':
    number_guessing()
elif number == '2':
    secure_password_generator()
elif number == '3':
    caesar_cipher()
elif number == '4':
    hangman()