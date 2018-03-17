""" Collation set """

import constant
import itertools


class CollationSet(object):
    """Collation set.

       Field:
          One example:
              [[1,2], [3], [4,5,6]]
    """

    def __init__(self, _collation_set):
        self._collation_set = _collation_set

    def to_matched_item_pairs(self):
        """ Convert collation set into a list of matched item pairs.

            Return:
                A list of item pairs. For example [[1,2], [3], [4,5,6]] is collation set,
                outputs of matched item pairs are
                [[1, 3], [2, 3], [1, 4], [1, 5], [1, 6], [3, 4], [3, 5], [3, 6]]
        """
        match_item_pairs = []
        for idx, match_item_id_arr in enumerate(self._collation_set):
            for match_item_id in match_item_id_arr:
                match_item_pairs.append(self.get_match_items(idx, match_item_id, self._collation_set))
        return match_item_pairs

    def get_match_items(self, index, item_id, match_list_arr):
        """
        :param index:
        :param match_list_arr:
        :return:

        get match items based on expert recommendation data
        """
        item_id = int(item_id)
        match_item_pairs = []
        for idx, match_item_ids in enumerate(match_list_arr):
            if idx == index:
                continue
            else:
                print("match_item_ids: %s" % match_item_ids)
                for match_item_id in match_item_ids:
                    print("match_item_id: %s" % match_item_id)
                    if match_item_id and len(match_item_id) > 0:
                        match_item_id = int(match_item_id)
                        match_item_pairs.append([min(item_id, match_item_id), max(item_id, match_item_id)])
                    else:
                        continue
        return match_item_pairs

    def to_matched_item_cat_pair(self, item_info):
        """ Convert collation set into a list of category pairs of matched item pairs.

            Args:
                item_info: a dictionary in which key is item_id, value is Item(item_id, category, image_path)

            Return:
                A list of category pairs. For example [[1,2], [3], [4,5,6]] is collation set,
                [[cat(1),cat(3)], [cat(2), cat(3)], [cat(1), cat(4)], [cat(1), cat(5)], [cat(1), cat(6)], [cat(3),
                  cat(4)], [cat(3), cat(5)], [cat(3), cat(6)]] here cat(item_id) is the category_id of item_id which
                can be obtained from item_info.
        """
        match_item_pairs = self.to_matched_item_pairs()
        match_item_cat_pairs = [None] * len(match_item_pairs)
        for index, item_pair in enumerate(match_item_pairs):
            item_cat_pair = [0] * 2
            for idx, item_id in enumerate(item_pair):
                item_cat_pair[idx] = item_info[item_id].get_cat_id()
            match_item_cat_pairs[index] = item_cat_pair
        return match_item_cat_pairs


if __name__ == '__main__':
    import util

    print 'Bingo'
    collation_list = [['1463018', '230955'],
                      ['1596334', '1704853'],
                      ['2226122', '284814', '36278', '480281']]
    match_set = CollationSet(collation_list)
    matched_item_pairs = match_set.to_matched_item_pairs()
    print matched_item_pairs
