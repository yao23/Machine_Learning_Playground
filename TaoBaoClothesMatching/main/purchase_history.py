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
        pairs = list(itertools.combinations(self._items, 2))
        ordered_pairs = [(min(first, second), max(first, second)) for first, second in pairs]
        return ordered_pairs

    def to_valid_item_pairs(self, item_info):
        if len(self._items) <= 10:
            pairs = list(itertools.combinations(self._items, 2))
            valid_item_pair = []
            for first, second in pairs:
                if first in item_info and second in item_info and item_info[first].get_cat_id() != item_info[second].get_cat_id():
                    valid_item_pair.append((min(first, second), max(first, second)))
            return valid_item_pair
        else:
            return []


if __name__ == '__main__':
    print 'Bingo'
