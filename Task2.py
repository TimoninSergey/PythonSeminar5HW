""" Создайте программу для игры в 'Крестики-нолики'
НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

 """

field = [1,2,3,
         4,5,6,
         7,8,9]

victory = [[0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]]

def print_field():
    print(field[0], end = " ")
    print(field[1], end = " ")
    print(field[2])
    print(field[3], end = " ")
    print(field[4], end = " ")
    print(field[5])
    print(field[6], end = " ")
    print(field[7], end = " ")
    print(field[8])  

def put_X0(X0, number):
    item = field.index(number)
    field[item] = X0


def check_win():
    winner = ''
    for i in victory:
        if field[i[0]] == field[i[1]] == field[i[2]] == 'X':
            winner = 'X'
        if field[i[0]] == field[i[1]] == field[i[2]] == '0':
            winner = '0'
    return winner


def game():
    player_1 = True
    win = False
    while win == False:
        print_field()
        if player_1 == True:
            X0 = 'X'
            field_num = int(input('Ход игрока 1: '))
        else:
            X0 = '0'
            field_num = int(input('Ход игрока 2: '))
        put_X0(X0, field_num)
        winner = check_win()
        if winner != '':
            win = True
        player_1 = not player_1
    print_field()
    print('Победил игрок ', winner)

game()

