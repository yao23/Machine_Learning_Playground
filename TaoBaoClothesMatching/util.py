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
    for image_folder in item_image_folders:  # TODO: assume image_folder is like "../data/image_data/img1"
        folder_arr = image_folder.split(constant.SLASH)
        image_name = folder_arr[-1]
        item_id = int(image_name[3:])
        item_image_dict[item_id] = image_folder + constant.ITEM_IMAGE_SUFFIX
    return item_image_dict


def load_item_info(item_info_path, item_image_folders):
    """ Item info.

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
            item_id = line_arr[0]
            category_id = line_arr[1]
            image_path = item_image_dict[item_id]
            item_dict[item_id] = Item(item_id, category_id, image_path)
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
            match_list_arr = match_list.split(';')
            collation_set = CollationSet(match_list_arr)
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
    purchase_history_dic = []
    with open(bought_history_path) as input_file:
        for line in input_file:
            line_arr = line.split(' ')
            user_id = line_arr[0]
            item_id = line_arr[1]
            purchase_history = PurchaseHistory(user_id, [item_id])
            purchase_history_dic[user_id] = purchase_history
        return purchase_history_dic


if __name__ == '__main__':
    print 'Bingo'
    # TODO: write some codes to test each function or write independent test class
    # like http://docs.python-guide.org/en/latest/writing/tests/
