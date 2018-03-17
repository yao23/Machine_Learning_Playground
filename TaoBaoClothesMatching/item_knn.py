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
        cat_pair_prob_dic = {}
        cat_pair_count_dic = {}
        cat_pair_set_dic = {}
        for cat_pair in matched_category_pairs:
            if cat_pair in cat_pair_count_dic:
                cat_pair_count_dic[cat_pair] += 1
            else:
                cat_pair_count_dic[cat_pair] = 1
            cat_one = cat_pair[0]
            cat_two = cat_pair[1]
            if cat_one in cat_pair_set_dic:
                cat_pair_set = cat_pair_set_dic[cat_one]
                if cat_two not in cat_pair_set:
                    cat_pair_set.add(cat_two)
                else:
                    continue
            else:
                cat_pair_set = set()
                cat_pair_set.add(cat_two)
                cat_pair_set_dic[cat_one] = cat_pair_set

        cat_pair_count = 0
        for cat_id, cat_pair_set in cat_pair_set_dic.items():
            if len(cat_pair_set) <= neigh_size:
                for match_cat_id in cat_pair_set:
                    cat_pair = (cat_id, match_cat_id)
                    cat_pair_count += cat_pair_count_dic[cat_pair]
                    cat_pair_prob_dic[cat_pair] = 0
            else:
                tmp_cat_pair_dic = {}
                for match_cat_id in cat_pair_set:
                    cat_pair = (cat_id, match_cat_id)
                    tmp_cat_pair_dic[cat_pair] = cat_pair_count_dic[cat_pair]
                tmp_cat_pair_counter = collections.Counter(tmp_cat_pair_dic)
                for cat_pair, cat_pair_count in tmp_cat_pair_counter.most_common(neigh_size):
                    cat_pair_count += cat_pair_count_dic[cat_pair]
                    cat_pair_prob_dic[cat_pair] = 0

        with open(constant.CATEGORY_MATCHING_FILE, 'a') as model_file:
            for cat_pair in cat_pair_prob_dic:
                probability = cat_pair_count_dic[cat_pair] / cat_pair_count
                cat_pair_prob_dic[cat_pair] = probability
                model_file.write(cat_pair[0] + ' ' + cat_pair[1] + ' ' + str(probability) + '\n')

        return cat_pair_prob_dic

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
        item_pair_prob_dic = {}
        item_pair_count_dic = {}
        item_pair_set_dic = {}
        for item_pair in purchased_item_pairs:
            if item_pair in item_pair_count_dic:
                item_pair_count_dic[item_pair] += 1
            else:
                item_pair_count_dic[item_pair] = 1
            item_one = item_pair[0]
            item_two = item_pair[1]
            if item_one in item_pair_set_dic:
                item_pair_set = item_pair_set_dic[item_one]
                if item_two not in item_pair_set:
                    item_pair_set.add(item_two)
                else:
                    continue
            else:
                item_pair_set = set()
                item_pair_set.add(item_two)
                item_pair_set_dic[item_one] = item_pair_set

        item_pair_count = 0
        for item_id, item_pair_set in item_pair_set_dic.items():
            if len(item_pair_set) <= neigh_size:
                for match_cat_id in item_pair_set:
                    item_pair = (item_id, match_cat_id)
                    item_pair_count += item_pair_count_dic[item_pair]
                    item_pair_prob_dic[item_pair] = 0
            else:
                tmp_item_pair_dic = {}
                for match_cat_id in item_pair_set:
                    item_pair = (item_id, match_cat_id)
                    tmp_item_pair_dic[item_pair] = item_pair_count_dic[item_pair]
                tmp_cat_pair_counter = collections.Counter(tmp_item_pair_dic)
                for item_pair, item_pair_count in tmp_cat_pair_counter.most_common(neigh_size):
                    item_pair_count += item_pair_count_dic[item_pair]
                    item_pair_prob_dic[item_pair] = 0

        with open(constant.ITEM_RELATIONSHIP_FILE, 'a') as model_file:
            for item_pair in item_pair_prob_dic:
                probability = item_pair_count_dic[item_pair] / item_pair_count
                item_pair_prob_dic[item_pair] = probability
                model_file.write(item_pair[0] + ' ' + item_pair[1] + ' ' + str(probability) + '\n')

        return item_pair_prob_dic

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
