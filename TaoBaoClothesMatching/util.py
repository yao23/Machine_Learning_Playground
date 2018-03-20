import constant
import glob
from item import Item
from collation_set import CollationSet
from purchase_history import PurchaseHistory


def load_item_image(item_image_folders):
    """Load item image.

       Args:
           item_image_folders: paths of item image folders.

        Returns:
            a dictionary of {item_id: item image path}
    """
    item_image_dict = {}
    for image_folder in item_image_folders:
        image_paths = glob.glob(image_folder + '/*' + constant.ITEM_IMAGE_SUFFIX)
        for item_path in image_paths:
            image_name_with_suffix = item_path.split(constant.SLASH)[-1]
            if len(image_name_with_suffix) >= 4 and image_name_with_suffix[-4:] == constant.ITEM_IMAGE_SUFFIX:
                item_id = image_name_with_suffix[:-4]
                item_image_dict[item_id] = item_path
    return item_image_dict


def load_item_info(item_info_path, item_image_folders):
    """ Load item info.

        Args:
           item_info_path: path of item information file.
           item_image_folders: folders of item images.

        Returns:
            {item_id: ITEM(id, cat_id, image_path)}
    """
    item_image_dict = load_item_image(item_image_folders)
    item_dict = {}
    with open(item_info_path) as input_file:
        for line in input_file:
            line_arr = line.split(' ')
            if len(line_arr) >= 3:
                item_id = line_arr[0]
                category_id = line_arr[1]
                if item_id in item_image_dict:
                    image_path = item_image_dict[item_id]
                else:
                    image_path = ''
                item_dict[item_id] = Item(item_id, category_id, image_path)
            else:
                continue
    return item_dict


def load_collation_set(collation_set_path):
    """ Load collation set.

        Args:
            collation_set_path: path of collation set file.

        Returns:
            a list of collation sets. For example
                [CollationSet([[1,2],[3],[4]]), CollationSet([[1],[9],[5]]), ....]
    """
    collation_set_list = []
    with open(collation_set_path) as input_file:
        for line in input_file:
            line_arr = line.split(' ')
            match_list = line_arr[1]
            match_list_arr = match_list.split(constant.SEMICOLON)
            match_set_list = [None] * len(match_list_arr)
            for index, match_set in enumerate(match_list_arr):
                match_set_list[index] = match_set.split(constant.COMMA)
            collation_set = CollationSet(match_set_list)
            collation_set_list.append(collation_set)
        return collation_set_list


def load_bought_history(bought_history_path):
    """ Load bought history records.

        Args:
            bought_history_path: path of match set file.

        Returns:
            a dictionary of purchased history. For example
            {user_id, BoughtHistory([1,2,3])}
    """
    purchase_history_dic = {}
    with open(bought_history_path) as input_file:
        for line in input_file:
            line_arr = line.split(' ')
            user_id = line_arr[0]
            item_id = line_arr[1]
            if user_id in purchase_history_dic:
                purchase_history_dic[user_id].add_one_item(item_id)
            else:
                purchase_history = PurchaseHistory(user_id, [item_id])
                purchase_history_dic[user_id] = purchase_history
        return purchase_history_dic


if __name__ == '__main__':
    print 'Bingo'
    item_info = load_item_info(constant.ITEM_INFO_FILE, constant.ITEM_IMAGE_PATHS)
    hist = load_bought_history(constant.BOUGHT_HISTORY)
    print hist['11322059'].to_valid_item_pairs(item_info)

    """
    item_info = read_item_info(constant.ITEM_FILE, constant.ITEM_IMAGE_PATHS)
    collations = read_match_set2(constant.MATCH_SET_FILE)

    cat_markov_chain = {}
    for collation in collations:
        match_set = MatchSet(collation)
        item_pair = match_set.to_collation_pairs()
        for first, second in item_pair:
            if item_info.has_key(first) and item_info.has_key(second):
                first_cat = item_info[first].get_item_cat_id()
                second_cat = item_info[second].get_item_cat_id()
                if first_cat > second_cat:
                    tmp = second_cat
                    second_cat = first
                    first_cat = tmp
                item_pair = first_cat + '-' + second_cat
                if cat_markov_chain.has_key(item_pair):
                    cat_markov_chain[item_pair] = cat_markov_chain[item_pair] + 1
                else:
                    cat_markov_chain[item_pair] = 1
    print cat_markov_chain
    """
