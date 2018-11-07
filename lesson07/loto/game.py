from lotto_bag import LottoBag
from card import LottoCard

__author__: str = 'Алексей Сидорюк'


class Game:
    def __init__(self, player_name, kegs_cnt):
        self._kegs_cnt = kegs_cnt
        # Берем мешочек с бочонками
        self._lb = LottoBag(kegs_cnt)
        # Выдаем карточку игроку
        self._card1 = LottoCard(kegs_cnt, player_name)
        # Машина рисует карточку себе
        self._card2 = LottoCard(kegs_cnt, 'Карточка компьютера.')
        self._result = [15, 15]

    def turn(self):
        # Вытаскиваем бочонок
        last_keg = self._lb.pool_one_keg()
        left_cnt = self._kegs_cnt - len(self._lb.show_open_kegs())
        for item in last_keg:
            print('\n', 'Новый бочонок: {} (осталось {})'.format(item, left_cnt), '\n')
        self._card1.show_card()
        self._card2.show_card()
        # Попробуем вычеркнуть номер с карточки машины
        if last_keg.issubset(self._lb.show_open_kegs()):
            self._result[1] = self._card2.cross_off_keg_num(last_keg)
        return [left_cnt, last_keg, self._result]

    def make_choice(self, keg_num):
        # Попробуем вычеркнуть номер с карточки игрока
        self._result[0] = self._card1.cross_off_keg_num(keg_num)
        return self._result[0]
