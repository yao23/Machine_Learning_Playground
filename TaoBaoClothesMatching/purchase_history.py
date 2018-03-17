""" Purchase history class. """

import itertools


class PurchaseHistory(object):
    def __init__(self, _user_id, _items):
        self._user_id = _user_id
        self._items = _items

    def get_user_id(self):
        return self._user_id

    def get_purchased_items(self):
        return self._items

    def add_one_item(self, item_id):
        self._items.append(item_id)

    def to_item_pairs(self):
        """ Convert items into a list of co-purchased item pairs.

            Return:
                A list of co-purchased item pairs. For example [1, 2, 3] is user's purchased items,
                outputs of co-purchased item pairs are
                [[1, 2], [1, 3], [2, 3]]
        """
        item_pairs = []
        item_set = set()
        for idx, item_id in enumerate(self._items):
            item_pair = self.get_item_pairs(idx, item_id, item_set)
            if item_pair:
                item_pairs.append(item_pair)
            else:
                continue
        return list(item_pairs)

    def get_item_pairs(self, index, cur_item_id, item_set):
        """
        :param index:
        :param cur_item_id:
        :param item_set:
        :return:

        get match items based on expert recommendation data
        """
        cur_item_id = int(cur_item_id)
        item_pairs = []
        for idx, item_id in enumerate(self._items):
            if idx == index:
                continue
            else:
                item_id = int(item_id)
                item_pair = [min(item_id, cur_item_id), max(item_id, cur_item_id)]
                item_pair_tuple = tuple(item_pair)
                if item_pair_tuple in item_set:
                    continue
                else:
                    item_set.add(item_pair_tuple)
                    item_pairs.append(item_pair)
        return item_pairs

    def to_valid_item_pairs(self, item_info):
        """ Get valid item pairs in purchase history

        :param item_info:
        :return:
        """
        if len(self._items) <= 10:
            pairs = list(itertools.combinations(self._items, 2))
            valid_item_pair = []
            for first, second in pairs:
                if first in item_info and second in item_info and \
                        item_info[first].get_cat_id() != item_info[second].get_cat_id():
                    valid_item_pair.append((min(first, second), max(first, second)))
            return valid_item_pair
        else:
            return []


if __name__ == '__main__':
    print 'Bingo'
    purchased_history = PurchaseHistory(_user_id='0001', _items=['1', '2', '3'])
    print purchased_history.to_item_pairs()
