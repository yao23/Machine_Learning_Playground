import constant
import util
import item_knn


class OfflineTrainer:
    """ Offline trainer to learn category matching and item relationship. """

    def __init__(self):
        """ Load trained model from local file

        """
        self.item_dict = util.load_item_info(constant.ITEM_INFO_FILE, constant.ITEM_IMAGE_PATHS)
        self.collation_set_list = util.load_collation_set(constant.COLLATION_SET_FILE)
        self.purchase_history_dic = util.load_bought_history(constant.BOUGHT_HISTORY)

    def train_category_model(self, k):
        """ Given k, train model to learn matching category relationship model.

            Args:
                k: number of most relevant categories
        """
        matched_category_pairs = []
        for collation_set in self.collation_set_list:
            cat_pair = collation_set.to_matched_item_cat_pair(self.item_dict)
            matched_category_pairs.append(cat_pair)
        item_knn.ItemKNN.learn_category_matching_relationship(matched_category_pairs, k)

    def train_item_model(self, k):
        """ Given k, train model to learn matching category relationship model.

            Args:
                k: number of most relevant items
        """
        purchased_item_pairs = []
        for user_id, purchase_history in self.purchase_history_dic:
            item_pairs = purchase_history.to_item_pairs()
            purchased_item_pairs.append(item_pairs)
        item_knn.ItemKNN.learn_item_relationship(purchased_item_pairs, k)


if __name__ == '__main__':
    print 'Bingo'
    k = 8
    offline_trainer = OfflineTrainer()
    offline_trainer.train_category_model(k)
    offline_trainer.train_item_model(k)
