from abc import ABCMeta, abstractmethod
import constant
import util
import heapq
import random


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
    """ Clothes matcher using item kNN.

        item kNN model includes two tables:
        (1) category to category matching relationships
             1       2      0.5
             1       5      0.3
             1       10     0.2


        (2) item to item matching relationships (purchased relationships)
             source item_id    matched item_id    similarity
             1001               1002                0.2
    """

    def __init__(self):
        """ Load trained model from local files

        """
        self._item_relationship_model = self._load_model(constant.ITEM_RELATION_FILE)
        self._cat_relationship_model = self._load_model(constant.CAT_RELATION_FILE)
        self._item_info = util.load_item_info(constant.ITEM_FILE, constant.ITEM_IMAGE_PATHS)

    def find_matched_clothes(self, source_item_id, k):
        """ Given a source item id, find its most matched k items.

            Args:
                source_item_id: source item id
                k: number of matched items
            Return:
                k matched items
        """
        if source_item_id not in self._item_info:
            return []

        # compute how many matched items in each category by category matching model
        cat_id = self._item_info[source_item_id].get_cat_id()
        if cat_id not in self._cat_relationship_model:
            return []
        cat_probs = self._cat_relationship_model[cat_id]
        num_matches_in_category = {}
        for k_round in range(k):
            sel_cat = self._tournament_selection(cat_probs)
            if sel_cat in num_matches_in_category:
                num_matches_in_category[sel_cat] = num_matches_in_category[sel_cat] + 1
            else:
                num_matches_in_category[sel_cat] = 1

        print num_matches_in_category
        print self._item_relationship_model[source_item_id]

        # return most matched items within each category
        matched_items = []
        for cat_key in num_matches_in_category.keys():
            top_k = num_matches_in_category[cat_key]
            matched_result_within_category = {}
            for item_key in self._item_relationship_model[source_item_id].keys():
                if item_key in self._item_info and self._item_info[item_key].get_cat_id() == cat_key:
                    matched_result_within_category[item_key] = self._item_relationship_model[source_item_id][item_key]

            print matched_result_within_category

            sel_item_ids = heapq.nlargest(top_k, matched_result_within_category)
            matched_items.extend(sel_item_ids)

        return matched_items

    def _load_model(self, model_file_name):
        model = {}
        with open(model_file_name, 'r') as f:
            for record in f:
                source_id, matched_id, prob = record.split(' ')
                if source_id not in model:
                    model[source_id] = {}
                model[source_id][matched_id] = float(prob)
        return model

    def _tournament_selection(self, probs):
        keys = probs.keys()
        acc_probs = [0] * len(keys)
        for index, key in enumerate(keys):
            if index == 0:
                acc_probs[index] = probs[key]
            else:
                acc_probs[index] = probs[key] + acc_probs[index - 1]

        a = random.random()
        index = 0
        while index < len(keys) and a > acc_probs[index]:
            index = index + 1
        return keys[index]


if __name__ == '__main__':
    matcher = ItemKNNMatcher()
    # matcher.find_matched_clothes('1258736', 10)
    # matcher.find_matched_clothes('2612866', 10)
    matcher.find_matched_clothes('1596334', 10)
