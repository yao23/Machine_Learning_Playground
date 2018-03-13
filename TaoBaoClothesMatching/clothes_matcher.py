from abc import ABCMeta, abstractmethod
import constant


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
        self.item_relationship_dic = []
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

    def find_matched_clothes(self, source_item, k):
        """ Given a source item id, find its most matched k items.

            Args:
                source_item: source item id
                k: number of matched items
        """
        if source_item in self.item_relationship_dic:
            match_item_set = self.item_relationship_dic[source_item]
            if len(match_item_set) <= k:
                return list(match_item_set)
            else:
                return list(match_item_set[:k+1])
        else:
            return []
