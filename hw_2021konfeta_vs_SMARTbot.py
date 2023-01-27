from random import randint
import myfunc.reg_players as rp
import myfunc.candies_checking as check

players_list = rp.reg_player_smartbot_names()
fate = randint(0, 1)
human_name = players_list[0]
bot_name = players_list[1]
candies_value = 345
if fate == 1:
    print(f'The first move is made by {human_name}')
    while candies_value > 0:
        if candies_value > 0:
            print(f'{candies_value} candies left')
            print(f'{human_name} please, make your move!')
            player_move_check = check.candies_checking()
            candies_value -= player_move_check
            p_move = True
        if candies_value > 0:
            print(f'{candies_value} candies left')
            bot_move = candies_value%29
            if bot_move == 0:
                bot_move = 1
            print(f'{bot_name} made his move and took {bot_move} candies!')
            candies_value -= bot_move
            p_move = False
        if candies_value < 0:
            candies_value = 0
    else:
        print(f'{candies_value} candies left')
        if p_move == True:
            print(f'{human_name} has won')
        else:
            print(f'{bot_name} has won')
else:
    print(f'The first move is made by {bot_name}')
    while candies_value > 0:
        if candies_value > 0:
            print(f'{candies_value} candies left')
            bot_move = candies_value%29
            print(f'{bot_name} made his move and took {bot_move} candies!')
            candies_value -= bot_move
            p_move = False
        if candies_value > 0:
            print(f'{candies_value} candies left')
            print(f'{human_name} please, make your move!')
            player_move_check = check.candies_checking()
            candies_value -= player_move_check
            p_move = True
        if candies_value < 0:
            candies_value = 0
    else:
        print(f'{candies_value} candies left')
        if p_move == True:
            print(f'{human_name} has won')
        else:
            print(f'{bot_name} has won')