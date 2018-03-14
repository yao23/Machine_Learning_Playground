from abc import ABCMeta, abstractmethod
import constant
import collections
import util
import item_knn


class ClothesMatcher(object):
    """ Interface for all kinds of clothes matcher.

    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def find_matched_clothes(self, source_item, k):
        """ Given a source item id, find its most matched k items.
        """
        pass


class ItemKNNMatcher(ClothesMatcher):
    """ Clothes matcher using item kNN. """

    def __init__(self):
        """ Load trained model from local file

        """
        self.item_dict = util.load_item_info(constant.ITEM_INFO_FILE, constant.ITEM_IMAGE_PATHS)
        self.collation_set_list = util.load_collation_set(constant.COLLATION_SET_FILE)
        self.purchase_history_dic = util.load_bought_history(constant.BOUGHT_HISTORY)

        self.item_pair_prob_dic = {}
        self.item_relationship_dic = {}
        with open(constant.ITEM_RELATIONSHIP_FILE) as input_file:
            for line in input_file:
                line_arr = line.split(' ')
                item_id = line_arr[0]
                match_item_id = line_arr[1]
                if item_id in self.item_relationship_dic:
                    match_item_set = self.item_relationship_dic[item_id]
                    match_item_set.add(match_item_id)
                else:
                    match_item_set = set()
                    match_item_set.add(match_item_id)
                    self.item_relationship_dic[item_id] = match_item_set
                self.item_pair_prob_dic[(item_id, match_item_id)] = line_arr[2]

    def find_matched_clothes(self, source_item, k):
        """ Given a source item id, find its most matched k items.

            Args:
                source_item: source item id
                k: number of matched items
        """
        matched_category_pairs = []
        for collation_set in self.collation_set_list:
            matched_category_pairs.append(collation_set.to_matched_item_cat_pair(self.item_dict))
        cat_pair_prob_dic = item_knn.ItemKNN.learn_category_matching_relationship(matched_category_pairs, k)

        purchased_item_pairs = []
        for user_id, purchase_history in self.purchase_history_dic:
            purchased_item_pairs.append(purchase_history.to_item_pairs())
        item_pair_prob_dic = item_knn.ItemKNN.learn_item_relationship(purchased_item_pairs, k)

        item = self.item_dict[source_item]
        category_id = item.get_cat_id()

        if source_item in self.item_relationship_dic:
            match_item_set = self.item_relationship_dic[source_item]
            if len(match_item_set) <= k:
                return list(match_item_set)
            else:
                tmp_item_pair_prob_dic = {}
                for match_item_id in match_item_set:
                    item_pair = (source_item, match_item_id)
                    tmp_item_pair_prob_dic[item_pair] = self.item_pair_prob_dic[item_pair]
                return list(collections.Counter(tmp_item_pair_prob_dic).most_common(k))
        else:
            return []
