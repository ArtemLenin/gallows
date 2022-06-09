import random

words = ['синхрофазотрон', 'дистрибьюция', 'множество']
correct_letters = set()
wrong_letters = set()

def show_word():
    for letter in word:
        print(letter if letter in correct_letters else '_', end=' ')
    print()

def show_game_interface():
    show_word()
    show_wrong_letters()

def show_wrong_letters():
    print("Использованные буквы: ", end='')
    for letter in wrong_letters:
        print(letter, end=' ')
    print()

def open_letter(letter):
    if letter not in correct_letters: 
        correct_letters.add(letter)
    else:
        print("Эта буква уже была")

def lose_heart(letter):
    global hearts
    hearts -= 1
    wrong_letters.add(letter)

def check_letter(letter):
    if (letter not in correct_letters and 
        letter not in wrong_letters):
        if letter in word:
            open_letter(letter)
        else:
            lose_heart(letter)
    else:
        print("Эта буква уже была")
        input()

hearts = 11
word = random.choice(words).lower()
while hearts > 0:
    show_game_interface()
    user_letter = input("Введите Вашу букву: ")
    letter = user_letter.lower()
    check_letter(letter)

    if correct_letters == set(word):
        show_word()
        print('Win!')
        break
else:
    print('Lose!')