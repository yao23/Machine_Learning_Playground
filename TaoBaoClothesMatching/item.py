""" Item class.

    Item has item-id, category-id and image path fields.

    Item has get_id, get_cat_id and show_image member functions.
"""


class Item(object):
    def __init__(self, _item_id, _cat_id, _item_image_path):
        self._item_id = _item_id
        self._cat_id = _cat_id
        self._item_image_path = _item_image_path

    def get_id(self):
        return self._item_id

    def get_cat_id(self):
        return self._cat_id

    def get_image_path(self):
        return self._item_image_path

    def show_image(self):
        # Future work
        return None


if __name__ == '__main__':
    item = Item('1', '298', '../data/image_data/img4')
    print item.get_id()
    print item.get_cat_id()
    print item.get_image_path()
