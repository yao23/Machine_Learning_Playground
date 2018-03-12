from abc import ABCMeta, abstractmethod


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
        # TODO finish codes of loading models from local file here.

    def find_matched_clothes(self, source_item, k):
        """ Given a source item id, find its most matched k items.

            Args:
                source_item: source item id
                k: number of matched items
        """
        # TODO finish codes of finding matched clothes there.
