import collections
import constant


class ItemKNN(object):

    @staticmethod
    def learn_category_matching_relationship(matched_category_pairs, neigh_size=5):
        """ Learn category matching relationship from collation set, and store them into a local file.

            Args:
                matched_category_pairs: a list of matched category pairs obtained from collation set.
                neigh_size: neighborhood size, for each source category, we only need to keep its more relevant top
                            neigh_size category.

            Return:
                a table with three columns like
                source category            matched category            probability
                1001                       1002                         0.2
                1001                       1005                         0.5
                1001                       1100                         0.3
                ...                        ...                          ...

                The above table is expected to be stored into a local file.
        """
        return ItemKNN.learn_pair_relationship_model(matched_category_pairs, neigh_size, constant.CATEGORY_MATCHING_FILE)

    @staticmethod
    def learn_item_relationship(purchased_item_pairs, neigh_size=20):
        """ Learn item matching relationship from purchased history, and store them into a local file.

            Args:
                purchased_item_pairs: a list of purchased item pairs obtained from item purchased history.
                neigh_size: neighborhood size, for each source item, we only need to keep its more relevant top
                            neigh_size items.

            Return:
                a table with three columns like
                source item              purchased item               probability
                1                         2                           0.15
                1                         8                           0.6
                1                         10                          0.15
                1                         20                          0.1

                The above table is expected to be stored into a local file.
        """
        return ItemKNN.learn_pair_relationship_model(purchased_item_pairs, neigh_size, constant.ITEM_RELATIONSHIP_FILE)

    @staticmethod
    def learn_pair_relationship_model(pairs, neigh_size=20, model_file_path=''):
        """ Learn category or item matching relationship from matching set or purchased history,
            and store them into a local file.

            Args:
                pairs: a list of category pairs obtained from matching set or
                       purchased item pairs obtained from item purchased history.
                neigh_size: neighborhood size, for each source category/item, we only need to keep its more relevant top
                            neigh_size categories/items.
                model_file_path: local path to write model file

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
        pair_probability_dic = {}
        pair_count_dic = {}
        pair_set_dic = {}
        for pair in pairs:
            if pair in pair_count_dic:
                pair_count_dic[pair] += 1
            else:
                pair_count_dic[pair] = 1
            pair_element_one = pair[0]
            pair_element_two = pair[1]
            if pair_element_one in pair_set_dic:
                pair_set = pair_set_dic[pair_element_one]
                if pair_element_two not in pair_set:
                    pair_set.add(pair_element_two)
                else:
                    continue
            else:
                pair_set = set()
                pair_set.add(pair_element_two)
                pair_set_dic[pair_element_one] = pair_set

        pair_count = 0
        for element_id, pair_set in pair_set_dic.items():
            if len(pair_set) <= neigh_size:
                for match_element_id in pair_set:
                    pair = (element_id, match_element_id)
                    pair_count += pair_count_dic[pair]
                    pair_probability_dic[pair] = 0
            else:
                tmp_pair_dic = {}
                for match_element_id in pair_set:
                    pair = (element_id, match_element_id)
                    tmp_pair_dic[pair] = pair_count_dic[pair]
                tmp_pair_counter = collections.Counter(tmp_pair_dic)
                for pair, pair_count in tmp_pair_counter.most_common(neigh_size):
                    pair_count += pair_count_dic[pair]
                    pair_probability_dic[pair] = 0

        with open(model_file_path, 'a') as model_file:
            for pair in pair_probability_dic:
                probability = 1.0 * pair_count_dic[pair] / pair_count
                pair_probability_dic[pair] = probability
                model_file.write(pair[0] + ' ' + pair[1] + ' ' + str(probability) + '\n')

        return pair_probability_dic
