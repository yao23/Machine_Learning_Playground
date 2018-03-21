import os
import util
import constant
from match_set import MatchSet
import heapq


class ItemKNN(object):
    @staticmethod
    def learn_category_matching_relationship(matched_category_pairs, neigh_size=5):
        """ Learn category matching relationship from collation set, and store them into a local file.

            Args:
                matched_category_pairs: a list of matched category pairs obtained from collation set.
                neigh_size: neighborhood size, for each source category, we only need to keep its more relevant top neigh_size category.

            Return:
                a table with three columns like
                source category            matched category            probability
                1001                       1002                         0.2
                1001                       1005                         0.5
                1001                       1100                         0.3
                ...                        ...                          ...

                The above table is expected to be stored into a local file.
        """
        ItemKNN.learn_pair_relationship(matched_category_pairs, neigh_size, constant.CAT_RELATION_FILE)

        return None

    @staticmethod
    def learn_item_relationship(purchased_item_pairs, neigh_size=20):
        """ Learn item matching relationship from purchased history, and store them into a local file.

            Args:
                purchased item paris: a list of purchased item pairs obtained from item purchased histogry.
                neigh_size: neighborhood size, for each source item, we only need to keep its more relevant top neigh_size items.

            Return:
                a table with three columns like
                source item              purchased item               probability
                1                         2                           0.15
                1                         8                           0.6
                1                         10                          0.15
                1                         20                          0.1

                The above table is expected to be stored into a local file.
        """
        ItemKNN.learn_pair_relationship(purchased_item_pairs, neigh_size, constant.ITEM_RELATION_FILE)

        return None

    @staticmethod
    def learn_pair_relationship(pairs, neigh_size=20, model_file_path=''):
        """ Learn category/item matching relationship from expert collation set or purchased history,
            and store them into a local file.

            Args:
                pairs: a list of category pairs / purchased item pairs obtained from collation set or
                       item purchased history.
                neigh_size: neighborhood size, for each source category / item, we only need to keep its more relevant
                            top neigh_size items.
                model_file_path: local file path to save model

            Return:
                a table with three columns like

                source category            matched category            probability
                1001                       1002                         0.2
                1001                       1005                         0.5
                1001                       1100                         0.3
                ...                        ...                          ...

                or

                source item              purchased item               probability
                1                         2                           0.15
                1                         8                           0.6
                1                         10                          0.15
                1                         20                          0.1

                The above table is expected to be stored into a local file.
        """
        pair_counts = {}
        frequency = {}
        for first, second in pairs:
            if (first, second) in pair_counts:
                pair_counts[(first, second)] = pair_counts[(first, second)] + 1
                pair_counts[(second, first)] = pair_counts[(second, first)] + 1
            else:
                pair_counts[(first, second)] = 1
                pair_counts[(second, first)] = 1

            if first in frequency:
                frequency[first] = frequency[first] + 1
            else:
                frequency[first] = 1

            if second in frequency:
                frequency[second] = frequency[second] + 1
            else:
                frequency[second] = 1

        # compute dense pairwise relationship
        output_model = {}
        for first, second in pair_counts.keys():
            if first not in output_model:
                output_model[first] = {}
            output_model[first][second] = 1.0 * pair_counts[(first, second)] / frequency[first]

        # compute sparse pairwise relationship by k-nearest neighbor and write it into a local file
        if os.path.exists(constant.ITEM_RELATION_FILE):
            os.remove(constant.ITEM_RELATION_FILE)

        with open(model_file_path, 'a') as output_file:
            for source_id in output_model.keys():
                keys = heapq.nlargest(neigh_size, output_model[source_id])
                sum_probabilities = 0.0
                for match_id in keys:
                    sum_probabilities = sum_probabilities + output_model[source_id][match_id]
                for match_id in keys:
                    output_file.write(str(source_id) + ' ' + str(match_id) + ' ' +
                                      str(output_model[source_id][match_id] / sum_probabilities) + '\n')

        return None


if __name__ == '__main__':

    # learn category relationship model
    match_sets = util.load_match_set(constant.MATCH_SET_FILE)
    item_info = util.load_item_info(constant.ITEM_FILE, constant.ITEM_IMAGE_PATHS)
    match_cat_pairs = []
    for match_set in match_sets:
        match_cat_pairs.extend(MatchSet.to_matched_cat_pairs(match_set.to_matched_item_pairs(), item_info))
    ItemKNN.learn_category_matching_relationship(match_cat_pairs)

    # learn item relationship model
    item_info = util.load_item_info(constant.ITEM_FILE, constant.ITEM_IMAGE_PATHS)
    purchase_history = util.load_bought_history(constant.BOUGHT_HISTORY)
    matched_item_pairs = []
    count = 1
    for items_from_one_user in purchase_history.values():
        matched_item_pairs.extend(items_from_one_user.to_valid_item_pairs(item_info))
        count = count + 1
        if count >= 100000:
            break
    ItemKNN.learn_item_relationship(matched_item_pairs)
