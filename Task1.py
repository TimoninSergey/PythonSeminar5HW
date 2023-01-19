""" Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит заданное количество конфет. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход.

a) Добавьте игру против бота

b) Подумайте как наделить бота 'интеллектом'

 """

import random

def player_vs_player(sweet_number):
    player1_score = 0
    player2_score = 0
    id = random.randint(1,2)
    player1 = False
    if id == 1:
        player1 = True
    while sweet_number > 0:
        move = 0
        if player1 == True:
            print('Ход 1-го игрока')
        else:
            print('Ход 2-го игрока')
        move = int(input('Введите число конфет, которые забираете (не более 28): '))
        if move > 28: 
            print('Не более 28')
            move = int(input('Введите число конфет, которые забираете (не более 28): '))
        elif move > sweet_number:
            print('Нет столько конфет, есть максимум {}'.format(sweet_number))
            move = int(input('Введите число конфет, которые забираете (не более 28): '))
        else:
            if player1 == True:
                player1_score = player1_score + move
                sweet_number = sweet_number - move
            else:
                player2_score = player2_score + move
                sweet_number = sweet_number - move
        player1 = not player1
        print('Осталось {} конфет'.format(sweet_number))
        print('Игрок 1 - {} конфет'.format(player1_score))
        print('Игрок 2 - {} конфет'.format(player2_score))
    if player1_score > player2_score:
        print('Конфеты закончились, победил игрок 1')
    elif player1_score == player2_score:
        print('Конфеты закончились, ничья')
    else:
        print('Конфеты закончились, победил игрок 2')

def player_vs_bot(sweet_number):
    player_score = 0
    bot_score = 0
    id = random.randint(1,2)
    player = False
    if id == 1:
        player = True
    while sweet_number > 0:
        move = 0
        if player == True:
            print('Ход игрока')
            move = int(input('Введите число конфет, которые забираете (не более 28): '))
            if move > 28: 
                print('Не более 28')
                move = int(input('Введите число конфет, которые забираете (не более 28): '))
            elif move > sweet_number:
                print('Нет столько конфет, есть максимум {}'.format(sweet_number))
                move = int(input('Введите число конфет, которые забираете (не более 28): '))
            else:
                player_score = player_score + move
                sweet_number = sweet_number - move
            player = not player
            print('Осталось {} конфет'.format(sweet_number))
            print('Игрок - {} конфет'.format(player_score))
            print('Бот - {} конфет'.format(bot_score))
        else:
            print('Ход бота')
            if sweet_number < 28:
                move = random.randint(1,sweet_number)
            else:
                move = random.randint(1,28)
            print('Бот забирает {} конфет'.format(move))
            bot_score = bot_score + move
            sweet_number = sweet_number - move
            print('Осталось {} конфет'.format(sweet_number))
            print('Игрок - {} конфет'.format(player_score))
            print('Бот - {} конфет'.format(bot_score))
            player = not player
    if player_score > bot_score:
        print('Конфеты закончились, победил игрок')
    elif player_score == bot_score:
        print('Конфеты закончились, ничья')
    else:
        print('Конфеты закончились, победил бот')

def start_game():
    num = int(input('Введите 1 для игры против бота и 2 для игры с человеком'))
    sweet_number = int(input('Введите количество конфет'))
    if num == 1:
        player_vs_bot(sweet_number)
    if num == 2:
        player_vs_player(sweet_number)

start_game()