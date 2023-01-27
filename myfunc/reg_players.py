from random import choice
# регистрация 2х игроков
def reg_player_names():
    count = 0
    players_list = []
    while count != 2:
        players_input = input(f'input name of the {count+1} player: ')
        players_list.append(f'{players_input}_id({count+1})')
        count += 1
    return players_list

#регистрация 1 игрока и глупого бота
def reg_player_sillybot_names():
    players_list = []
    player_input = input("Input your name, pls: ")
    players_list.append(f'{player_input}_user')
    bot_names = ['Billy', 'Willy', 'Dilly', 'Milly']
    players_list.append(f'{choice(bot_names)}_bot')
    return players_list

#регистрация 1 игрока и умного бота
def reg_player_smartbot_names():
    players_list = []
    player_input = input("Input your name, pls: ")
    players_list.append(f'{player_input}_user')
    bot_names = ['Isaak_Newton', 'Albert_Einstein', 'Max_Planck', 'Marie_Curie']
    players_list.append(f'{choice(bot_names)}_bot')
    return players_list