import random

__author__: str = 'Алексей Сидорюк'


class LottoBag:
    def __init__(self, kegs):
        self._kegs = kegs
        self._open_kegs = set()

    def pool_one_keg(self):
        if self._kegs - len(self._open_kegs) > 0:
            # Делаем вид, что вытаскиваем бочонок из мешочка.
            keg_tmp = {random.randint(1, self._kegs)}
            # На самом деле ищем номер не из списка уже объявленных.
            while keg_tmp.issubset(self._open_kegs):
                keg_tmp = {random.randint(1, self._kegs)}
            # после чего keg - первый попавшийся бочонок, номер которого еще не был объявлен, добавляем к открытым
            self._open_kegs = self._open_kegs | keg_tmp
            # и "показываем" его
            return keg_tmp

    def show_open_kegs(self):
        return self._open_kegs
