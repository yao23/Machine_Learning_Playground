""" Collation set """

import constant
import itertools


class MatchSet(object):
    """Match set.

       One example:
           [[1,2], [3], [4,5,6]]
    """

    def __init__(self, _match_set):
        self._match_set = _match_set

    def to_matched_item_pairs(self):
        match_item_pairs = []
        matched_group_pairs = list(itertools.combinations(self._match_set, 2))
        for first_group, second_group in matched_group_pairs:
            match_item_pairs.extend(list(itertools.product(first_group, second_group)))
        return match_item_pairs

    @staticmethod
    def to_matched_cat_pairs(match_item_pairs, item_info):
        matched_cat_pairs = []
        for first_item, second_item in match_item_pairs:
            if first_item in item_info and second_item in item_info:
                first_item_cat_id = item_info[first_item].get_cat_id()
                second_item_cat_id = item_info[second_item].get_cat_id()
                matched_cat_pairs.append(
                    (min(first_item_cat_id, second_item_cat_id), max(first_item_cat_id, second_item_cat_id)))
        return matched_cat_pairs


if __name__ == '__main__':
    import util

    print 'Bingo'
    collation_list = [['1463018', '230955'],
                      ['1596334', '1704853'],
                      ['2226122', '284814', '36278', '480281']]
    match_set = MatchSet(collation_list)
    matched_item_pairs = match_set.to_matched_item_pairs()
    item_info = util.load_item_info(constant.ITEM_FILE, constant.ITEM_IMAGE_PATHS)
    print MatchSet.to_matched_cat_pairs(matched_item_pairs, item_info)
