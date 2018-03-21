import constant
import glob
from item import Item
from match_set import MatchSet
from purchase_history import PurchaseHistory


def load_item_image(item_image_folders):
    """Load item image.

       Args:
           item_image_folders: paths of item image folders.

        Returns:
            {item_id: item image path}
    """
    image_path_dict = {}
    for folder in item_image_folders:
        image_paths = glob.glob(folder + '/*' + constant.ITEM_IMAGE_SUFFIX)
        for item_path in image_paths:
            image_name_with_suffix = item_path.split(constant.SLASH)[-1]
            if len(image_name_with_suffix) >= 4 and image_name_with_suffix[-4:] == constant.ITEM_IMAGE_SUFFIX:
                id = item_path.split(constant.SLASH)[-1][:-4]
                image_path_dict[id] = item_path
    return image_path_dict


def load_item_info(item_info_path, item_image_folders):
    """ Item info.

        Args:
           item_info_path: path of item information file.
           item_image_folders: folders of item images.

        Returns:
            {item_id: ITEM(id, cat_id, image_path)}
    """
    item_images = load_item_image(item_image_folders)
    item_infos = {}
    with open(item_info_path, 'r') as f:
        for item_info in f:
            fields_in_item_info = item_info.split()
            if len(fields_in_item_info) >= 3:
                id = fields_in_item_info[0]
                cat_id = fields_in_item_info[1]
                if item_images.has_key(id):
                    item_infos[id] = Item(id, cat_id, item_images[id])
                else:
                    item_infos[id] = Item(id, cat_id, None)
    return item_infos


def load_match_set(match_set_path):
    """ Load item match set.

        Args:
            match_set_path: path of match set file.

        Returns:
            a list of match sets. For example
                [[[1,2],[3],[4]], [[1],[9],[5]]]
    """
    match_sets = []
    with open(match_set_path, 'r') as f:
        for match_set_as_string in f:
            match_set = match_set_as_string.split()[1].split(constant.SEMICOLON)
            match_set_as_list_list = [items_as_string.split(constant.COMMA) for items_as_string in match_set]
            match_sets.append(MatchSet(match_set_as_list_list))
    return match_sets


def load_bought_history(bought_history_path):
    hist = {}
    with open(bought_history_path, 'r') as f:
        for bought_items_as_string in f:
            user_id, item_id, _ = bought_items_as_string.split()
            if user_id not in hist:
                hist[user_id] = PurchaseHistory(user_id, [])
            hist[user_id].add_one_item(item_id)

    return hist


if __name__ == '__main__':
    print 'Bingo'
    item_info = load_item_info(constant.ITEM_FILE, constant.ITEM_IMAGE_PATHS)
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
