from game import Game

__author__: str = 'Алексей Сидорюк'


player_name = 'Алексей'
kegs_cnt = 90

lets_play = Game(player_name, kegs_cnt)

while True:
    game_state = lets_play.turn()
    if game_state[0] != 0:
        choice = input('Вычеркнуть номер на карточке? [y/n]: ')
        gs_tmp = game_state[2][0]
        if choice == 'y':
            if lets_play.make_choice(game_state[1]) == gs_tmp:
                print('Вы проиграли. В вашей карточке нет номера', game_state[1])
                break
        elif choice == 'n':
            if lets_play.make_choice(game_state[1]) < gs_tmp:
                if game_state[2][0] > 0:
                    print('Вы проиграли. В вашей карточке был номер', game_state[1])
                    break
        else:
            print('Хорошо, сыграем в другой раз.')
            break
        if game_state[2][0] == 0 and game_state[2][1] >= 0:
            print('Поздравляю с победой!')
            break
        elif game_state[2][0] > 0 and game_state[2][1] == 0:
            print('Бездушная машина победила...')
            break
    else:
        break
