import random

__author__: str = 'Алексей Сидорюк'


class LottoCard:
    def __init__(self, kegs, gamer_name):
        self._gamer_name = gamer_name
        self._number_set = set()

        # Подготовим строки карточки
        while len(self._number_set) < 15:
            self._number_set = self._number_set | {random.randint(1, kegs)}
        self._card_list = list(self._number_set)

        def make_card_string_from_list(lst):
            lst.sort()
            l9 = [' ']*9
            pos = random.randint(0, 9 - len(lst))
            for itm, el in enumerate(lst):
                l9[pos] = str(el)
                pos = random.randint(pos + 1, 9 - len(lst) + itm + 1)
            return l9

        self._card_rows_str = [
            make_card_string_from_list(self._card_list[:5]),
            make_card_string_from_list(self._card_list[5:-5]),
            make_card_string_from_list(self._card_list[-5:])
            ]

    # Нарисуем карточку
    def show_card(self):
        print('{:-^22}'.format(self._gamer_name))
        for row in self._card_rows_str:
            print(' '.join(row))
        print('{:-^22}'.format('-'), '\n')

    # Проверим, номер бочонка есть на карточке?
    def isincard(self, keg_num):
        return True if keg_num.issubset(self._number_set) else False

    # Вычеркнем номер бочонка из карточки, если номер совпал. Показываем, сколько осталось невычеркнутых.
    def cross_off_keg_num(self, keg_num):
        if self.isincard(keg_num):
            self._number_set -= keg_num
            for row in self._card_rows_str:
                for item in keg_num:
                    if str(item) in row:
                        row[row.index(str(item))] = '-'
        return len(self._number_set)
