import random


def Number_Guessing():
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
        Number_Guessing()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

def Magic_ball_8():
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

print('Доброго времени суток. Как тебя зовут?')
name = input()
print('Здравствуй, ', name, '. Что ты хочешь запустить? Напиши номер программы', '1) Угадайка чисел', sep = '')
if input() == '1':
    Number_Guessing()
if input() == '2':
