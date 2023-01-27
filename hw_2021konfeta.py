# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint
import myfunc.reg_players as rp
import myfunc.candies_checking as check

# определение очередности хода
players_list = rp.reg_player_names()
player_1_name = randint(0, 1)

if player_1_name == 1:
    player_1_name = players_list[0]
    player_2_name = players_list[1]
    print(f'The first move is made by {player_1_name}')
else:
    player_1_name = players_list[1]
    player_2_name = players_list[0]
    print(f'The first move is made by {player_1_name}')

# ходы по очереди
candies_value = 345
while candies_value > 0:
    if candies_value > 0:
        print(f'{candies_value} candies left')
        print(f'{player_1_name} please, make your move!')
        player_move_check = check.candies_checking()
        candies_value -= player_move_check
        p_move = True
    if candies_value > 0:
        print(f'{candies_value} candies left')
        print(f'{player_2_name} please, make your move!')
        player_move_check = check.candies_checking()
        candies_value -= player_move_check
        p_move = False
    if candies_value < 0:
        candies_value = 0
else:
    print(f'{candies_value} candies left')
    if p_move == True:
        print(f'{player_1_name} has won')
    else:
        print(f'{player_2_name} has won')
